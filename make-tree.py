import logging
import os
from dotenv import load_dotenv
from openai import OpenAI
import itertools
import re

# .envファイルをロードして環境変数を読み込む
load_dotenv()

# 環境変数からAPIキーを取得
client =  OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 入力ファイルと出力ディレクトリのパスを設定
input_file_path = "Generated_NonRequirements/non_requirements_definition.md"  # Replace with the path to your input markdown file
base_path = "Requirements/FR"  # Replace with the path to your desired output directory

# シナリオへのパスを設定
additional_file = "Requirements/Scenario.md"

# フォルダが存在しない場合は作成する
if not os.path.exists(base_path):
    os.makedirs(base_path)

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def create_structure(base_path, structure):
    current_folder = ""
    current_file_path = None  # 初期化
    current_file_content = ""
    files_created = []
    lines = structure.strip().split('\n')
    
    for line in lines:
        if line.startswith("## "):  # Folder level
            if current_file_content and current_file_path:  # ここでファイルを書き込む
                with open(current_file_path, 'w', encoding='utf-8') as f:
                    f.write(current_file_content)
                files_created.append(current_file_path)
                #logging.info(f"Created file: {current_file_path}")
            current_folder = line[3:].strip()
            current_folder_path = os.path.join(base_path, current_folder)
            os.makedirs(current_folder_path, exist_ok=True)
            current_file_content = line + "\n"
            #current_file_path = os.path.join(current_folder_path, current_folder + ".md")  # フォルダレベルでファイルパスを設定
            #logging.info(f"Creating folder: {current_folder_path}")
        elif line.startswith("### "):  # Sub-folder level
            if current_file_content and current_file_path:  # ここでファイルを書き込む
                with open(current_file_path, 'w', encoding='utf-8') as f:
                    f.write(current_file_content)
                files_created.append(current_file_path)
                #logging.info(f"Created file: {current_file_path}")
            sub_folder = line[4:].strip()
            current_file_path = os.path.join(current_folder_path, sub_folder + ".md")  # サブフォルダレベルでファイルパスを設定
            current_file_content = line + "\n"
            #logging.info(f"Creating sub-folder file: {current_file_path}")
        else:
            current_file_content += line + "\n"
    
    if current_file_content and current_file_path:  # 最後のファイルを書き込む
        with open(current_file_path, 'w', encoding='utf-8') as f:
            f.write(current_file_content)
        files_created.append(current_file_path)
        #logging.info(f"Created final file: {current_file_path}")
    
    return files_created

def generate_functional_specifications(files):
    #logging.info("Generating functional specifications...")
    # 全ての組み合わせを生成（空集合を除く）
    combinations = []
    for i in range(1, len(files) + 1):
        combinations.extend(itertools.combinations(files, i))

    # 各組み合わせについて、非機能要求書を生成して保存
    for combination in combinations:
        combined_content = ""
        filenames_in_prompt = "と".join([os.path.basename(f) for f in combination])
        
        for file_path in combination:
            with open(file_path, 'r', encoding='utf-8') as file:
                combined_content += file.read() + "\n\n"
        
        prompt = f"以下の{filenames_in_prompt}を参考にして機能要求書を作成してください。\n\n{combined_content}"

        # OpenAI APIを使って機能要求書を生成
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        generated_text = response.choices[0].message.content
        #logging.info(f"Generated text for combination: {filenames_in_prompt}")

        # 結果を新しいファイルに保存
        sanitized_filenames = "_".join([os.path.splitext(os.path.basename(f))[0] for f in combination])
        output_file_path = os.path.join(base_path, "combinations", f"{sanitized_filenames}.md")
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(generated_text)
        #logging.info(f"Saved generated file: {output_file_path}")

    #logging.info("機能要求書の生成が完了しました。")

def list_markdown_files(folder_path):
    markdown_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                markdown_files.append(file_path)
    return markdown_files

def main():
    #logging.info("Starting process...")
    # Read the content of the input markdown file
    #content = read_markdown_file(input_file_path)
    
    # Create the directory structure based on the markdown content
    #従来はこっち
    #files_created = create_structure(base_path, content)

    #フォルダからリスト
    folder_path="Requirements"
    markdown_files = list_markdown_files(folder_path)
    
    # Generate functional specifications for each file created
    generate_functional_specifications(markdown_files)
    #logging.info("Process completed.")

if __name__ == "__main__":
    main()
