import uuid
import pymysql


def generateActivationCode(num):
    codeList = []
    for i in range(num):
        code = str(uuid.uuid4()).replace('-', '').upper()
        while code in codeList:
            code = str(uuid.uuid4()).replace('-', '').upper()
        codeList.append(code)
    return codeList


if __name__ == '__main__':
    generateActivationCode(200)
