# Created by Zhiyuan Li on 2024 Aug 31.
# Only for personal uses

import os
import requests
from urllib.parse import urljoin

def download_pdfs(url_list, download_folder):
    # 创建下载文件夹，如果文件夹不存在
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for url in url_list:
        try:
            # 处理URL以获取文件名
            filename = os.path.join(download_folder, os.path.basename(url))
            
            # 发起请求获取PDF内容
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功

            # 将PDF内容写入文件
            with open(filename, 'wb') as pdf_file:
                pdf_file.write(response.content)
            
            print(f'Successfully downloaded: {filename}')
        
        except requests.exceptions.RequestException as e:
            print(f'Failed to download {url}: {e}')

def get_urllinks(name):
    # 因为是小程序，就在内部生成了
    re = []
    # types = [""]
    types = ["Contest","Solution"]
    for year in range(1996,2025 ,1):
        for tp in types:
            re.append(f"https://cemc.uwaterloo.ca/sites/default/files/documents/{year}/{year}{name}{tp}.pdf")
    return re

def get_urllinks_COMC(name):
    # 因为是小程序，就在内部生成了
    re = []
    types = [""]
    # types = ["Contest","Solution"]
    for year in range(1996,2024 ,1):
        for tp in types:
            re.append(f"https://cms.math.ca/wp-content/uploads/2023/01/comc{year}-exam-en.pdf")
            re.append(f"https://cms.math.ca/wp-content/uploads/2023/01/comc{year}-official-solutions-en.pdf")
    return re

if __name__ == "__main__":
    # names is a list
    # names = ["CSMC","CIMC"]
    # names = ["Hypatia","Galois","Fryer","Euclid"]
    names = ["COMC"]
    for name in names:
        # pdf_urls = get_urllinks(name)
        pdf_urls = get_urllinks_COMC(name)
        download_folder = f'./{name}_pdf_downloads'
        download_pdfs(pdf_urls, download_folder)
