import PyPDF2
from reportlab.pdfgen import canvas


def add_watermark(input_pdf, output_pdf, watermark_text):
    # 创建一个带有文本的PDF文件，作为水印
    watermark_pdf = "watermark.pdf"
    with open(watermark_pdf, 'wb') as watermark_file:
        pdf_canvas = canvas.Canvas(watermark_file)
        pdf_canvas.drawString(100, 100, watermark_text)
        pdf_canvas.save()

    # 打开原始PDF文件
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        # 打开水印PDF文件
        with open(watermark_pdf, 'rb') as watermark_file:
            watermark_reader = PyPDF2.PdfReader(watermark_file)

            # 创建一个新的PDF写入对象
            pdf_writer = PyPDF2.PdfFileWriter()

            # 遍历每一页
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)

                # 获取对应水印页面
                watermark_page = watermark_reader.getPage(0)

                # 将水印合并到原始页面
                page.merge_page(watermark_page)
                pdf_writer.addPage(page)

            # 将结果写入输出PDF文件
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)


if __name__ == "__main__":
    # 输入PDF文件路径
    input_pdf_path = "input.pdf"
    # 输出PDF文件路径
    output_pdf_path = "output.pdf"
    # 水印文本
    watermark_text = "Confidential"

    # 调用添加水印函数
    add_watermark(input_pdf_path, output_pdf_path, watermark_text)
