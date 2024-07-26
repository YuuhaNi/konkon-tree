import os
from dotenv import load_dotenv
from openai import OpenAI
import re

# .envファイルをロードして環境変数を読み込む
load_dotenv()

# 環境変数からAPIキーを取得
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# 初期提案書の内容を読み込む
initial_proposal_path = os.path.join('Requirements_Phase', '01_Initial_Proposal_ja.md')
with open(initial_proposal_path, 'r', encoding='utf-8') as file:
    initial_proposal_content = file.read()

# 構造を読み込む
structure_path = '非機能要求構造.md'
with open(structure_path, 'r', encoding='utf-8') as file:
    structure_content = file.read()

# 要件定義書の生成
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", 
        "content": f"あなたはプロのエンジニアです。次のシナリオから非機能要件の全要素を詳細に記述し作成を行ってください。\n"
                f"内容はこれで開発を進めていくので構造・項目を参考にわかりやすく、省略せずに詳細に作成してください。\n"
                f"シナリオ: {initial_proposal_content}\n"
                f"要件定義書の構造: {structure_content}\n"
                "図を作成する場合はPlantUMLで記述\n"
                "参考文献はIPAの非機能要求グレード 2018です。"
        }
    ]
)

requirements_definition = response.choices[0].message.content

# 要件定義書全体を保存する
output_dir = 'Generated_NonRequirements'
os.makedirs(output_dir, exist_ok=True)

requirements_path = os.path.join(output_dir, 'requirements_definition.md')
with open(requirements_path, 'w', encoding='utf-8') as file:
    file.write(requirements_definition)

# # セクションごとに分割する関数
# def split_sections(md_content):
#     sections = []
#     current_section = []
#     for line in md_content.split('\n'):
#         if line.startswith('##'):  # 見出しでセクションを分ける
#             if current_section:
#                 sections.append('\n'.join(current_section))
#                 current_section = []
#         current_section.append(line)
#     if current_section:
#         sections.append('\n'.join(current_section))
#     return sections

# # セクションごとに分割
# sections = split_sections(requirements_definition)

# # 各セクションを適切なフォルダに保存
# current_folder = output_dir

# for section in sections:
#     # 最初の見出し行を取得
#     first_line = section.split('\n')[0]
#     if first_line.startswith('### '):
#         # トップレベルの見出しの場合、新しいフォルダを作成
#         current_folder = os.path.join(output_dir, re.sub(r'[^\w\s-]', '', first_line[4:].strip()).replace(' ', '_'))
#         os.makedirs(current_folder, exist_ok=True)
#     elif first_line.startswith('##### '):
#         # サブレベルの見出しの場合、ファイル名を生成
#         filename = re.sub(r'[^\w\s-]', '', first_line[5:].strip()).replace(' ', '_') + '.md'
#         file_path = os.path.join(current_folder, filename)
#         with open(file_path, 'w', encoding='utf-8') as file:
#             file.write(section)

print(f"要件定義書全体が{requirements_path}に保存されました。")
print(f"各セクションが{output_dir}ディレクトリに保存されました。")