# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define :servidorWeb do |servidorWeb|
    servidorWeb.vm.box = "bento/ubuntu-22.04"
    servidorWeb.vm.network :private_network, ip: "192.168.80.3"
    servidorWeb.vm.provision "file", source: "frontend", destination: "/home/vagrant/api/frontend"
    servidorWeb.vm.provision "file", source: "microUsers", destination: "/home/vagrant/api/microUsers"
    servidorWeb.vm.provision "file", source: "microProducts", destination: "/home/vagrant/api/microProducts"
    servidorWeb.vm.provision "file", source: "microOrders", destination: "/home/vagrant/api/microOrders"
    servidorWeb.vm.provision "file", source: "docker-compose.yml", destination: "/home/vagrant/api/docker-compose.yml"
    servidorWeb.vm.provision "file", source: "init.sql", destination: "/home/vagrant/db/init.sql"
    servidorWeb.vm.provision "shell", path: "script.sh"
    servidorWeb.vm.hostname = "servidorWeb"
  end
end
