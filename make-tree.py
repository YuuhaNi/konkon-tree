import os
from dotenv import load_dotenv
from openai import OpenAI
import itertools
import re

# .envファイルをロードして環境変数を読み込む
load_dotenv()

# 環境変数からAPIキーを取得
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 機能要件フォルダへのパスを設定
folder_path = "Generated_Requirements/機能要件"
output_folder = "Generated_Requirements/機能要件_combinations"

# フォルダが存在しない場合は作成する
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 機能要件フォルダ内のrequirements_definition.mdを除く全てのMarkdownファイルを取得
md_files = [f for f in os.listdir(folder_path) if f.endswith(".md") and f != "requirements_definition.md"]

# 全ての組み合わせを生成（空集合を除く）
combinations = []
for i in range(1, len(md_files) + 1):
    combinations.extend(itertools.combinations(md_files, i))

# 各組み合わせについて、機能要求書を生成して保存
for idx, combination in enumerate(combinations):
    combined_content = ""
    filenames_in_prompt = "と".join(combination)
    
    for filename in combination:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            combined_content += file.read() + "\n\n"
    
    prompt = f"{filenames_in_prompt}を組み合わせて機能要求書を作成してください。\n\n{combined_content}"

    # OpenAI APIを使って機能要求書を生成
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    generated_text = response.choices[0].message.content

    # 結果を新しいファイルに保存
    sanitized_filenames = "_".join([os.path.splitext(f)[0] for f in combination])
    output_file_path = os.path.join(output_folder, f"{sanitized_filenames}.md")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(generated_text)

print("機能要求書の生成が完了しました。")