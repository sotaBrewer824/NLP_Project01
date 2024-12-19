import os
from pdf2image import convert_from_path

def pdf_to_images_in_directory(output_folder="output_images", dpi=300):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取当前目录下的所有 PDF 文件
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the current directory.")
        return

    # 遍历每个 PDF 文件
    for pdf_file in pdf_files:
        print(f"Processing {pdf_file}...")
        try:
            # 将 PDF 转换为图像
            images = convert_from_path(pdf_file, dpi=dpi)

            # 保存每页图像
            for i, image in enumerate(images):
                output_path = os.path.join(output_folder, f"{os.path.splitext(pdf_file)[0]}_page_{i + 1}.png")
                image.save(output_path, 'PNG')
                print(f"Saved: {output_path}")
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")

if __name__ == "__main__":
    pdf_to_images_in_directory()
