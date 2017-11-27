#coding:utf-8

import os
try:
    import paramiko
except ImportError:
    from TicketBusinessLibrary.libs import paramiko

class File():
    def __init__(self):
        pass

    def _get_php_config_key_value(self,server_ip,remote_path,keyname):
        '''
        获取服务器中config.php中的keyname的值
        '''
        local_path = u"D:/config.php"
        client = paramiko.Transport((server_ip,22))
        client.connect(username="root",password="pw#1905")
        sftp = paramiko.SFTPClient.from_transport(client)
        sftp.get(remote_path,local_path)
        client.close()

        f = open(local_path,"r")
        lines = f.readlines()
        for line in lines:
            line = line,
            line = line[0].strip()
            liness = line.split("=>")
            liness[0] = liness[0].strip().replace("'",'').replace('"','')
            if liness[0] == keyname:
                f.close()
                os.remove(local_path)
                return liness[1].strip().replace("'",'').replace(",",'').replace('"','')


if __name__ == "__main__":
    a = File()._get_php_config_key_value()
