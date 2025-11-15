import setuptools
from pathlib import Path

# собираем только файлы (исключаем директории)
package_files = [
    str(p).replace("iopaint/", "")
    for p in Path("iopaint/web_app").rglob("*")
    if p.is_file()
]

# дополнительные файлы (если они лежат вне пакета iopaint, оставляем с относительным путём)
package_files += [
    "model/anytext/ocr_recog/ppocr_keys_v1.txt",
    "model/anytext/anytext_sd15.yaml",
    "model/original_sd_configs/sd_xl_base.yaml",
    "model/original_sd_configs/sd_xl_refiner.yaml",
    "model/original_sd_configs/v1-inference.yaml",
    "model/original_sd_configs/v2-inference-v.yaml",
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def load_requirements():
    requirements_file_name = "requirements.txt"
    requires = []
    with open(requirements_file_name) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                requires.append(line)
    return requires

setuptools.setup(
    name="IOPaint",
    version="1.6.0",
    author="PanicByte",
    author_email="cwq1913@gmail.com",
    description="Image inpainting, outpainting tool powered by SOTA AI Model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sanster/IOPaint",
    # обычный и надёжный вызов
    packages=setuptools.find_packages(),
    # ВАЖНО: include_package_data=True разрешает включать файлы, перечисленные в MANIFEST.in
    include_package_data=True,
    package_data={"iopaint": package_files},
    install_requires=load_requirements(),
    python_requires=">=3.7",
    entry_points={"console_scripts": ["iopaint=iopaint:entry_point"]},
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
