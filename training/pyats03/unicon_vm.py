from unicon import Connection

# help(Connection)
vm = Connection(hostname='vm424583', start=['ssh 192.168.242.44'],
                username='pyast', password='pyastpyast', os='linux')
vm.connect()
vm.connected
version = vm.execute('cat /etc/issue')
version
vm.disconnect()
