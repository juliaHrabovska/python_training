import json
import threading
import requests


response_info_list = []


def get_status_code_of_link(link):
    try:
        response = requests.get(link)
        response_info_list.append(
            {
                "url": link,
                "is_ok": response.status_code < 400,
                "status_code": response.status_code
            }
        )
    except (Exception):
        response_info_list.append(
            {
                "url": link,
                "is_ok": False,
                "status_code": None
            }
        )


def get_links():
    file = open("links.txt", "r")
    links = file.readlines()
    file.close()

    return list(map(lambda link: link.replace("\n", ""), links))


def run_all_verification_in_parallel():
    for link in get_links():
        thread = threading.Thread(target=get_status_code_of_link, args=(link,))
        thread.start()
        thread.join()

    with open('result.json', 'w') as json_file:
        json.dump(response_info_list, json_file, indent=2)


if __name__ == '__main__':
    run_all_verification_in_parallel()
