# Deploy Semaphore Role

This Ansible role is designed to deploy Semaphore, an open-source web-based solution for Ansible playbooks. Below are the manual steps necessary to configure and start Semaphore.
## Prerequisites

1. **Clone this repository:**
  ```sh
  git clone https://github.com/all-things-automated/ansible.git
  ```

2. **Ensure the inventory is accurate for your environment:**
  Review and update the `inventory` file in the cloned repository to match your environment settings.

3. **Execute the Ansible playbook:**
  ```sh
  ansible-playbook -i {{ your_inventory }} deploy-semaphore.yml -u {{ ansible_user }} --ask-pass --ask-become-pass
  ```

## Manual Steps
This Ansible role is designed to deploy Semaphore, an open-source web-based solution for Ansible playbooks. Below are the manual steps necessary to configure and start Semaphore.

### MariaDB Configuration

1. **Run the MariaDB secure installation script:**
  ```sh
  sudo mariadb-secure-installation
  ```

2. **Follow the prompts:**
  ```
  Switch to unix_socket authentication [Y/n] n
  Change the root password? [Y/n] y
  Remove anonymous users? [Y/n] y
  Disallow root login remotely? [Y/n] y
  Remove test database and access to it? [Y/n] y
  Reload privilege tables now? [Y/n] y
  ```

### Semaphore Setup following MariaDB Configuarion

1. **Create the systemd service file for Semaphore:**
  ```sh
  sudo vim /etc/systemd/system/semaphore.service
  ```
  Add the following content to the file:
  ```
  [Unit]
  Description=Semaphore Ansible UI
  Documentation=https://github.com/ansible-semaphore/semaphore
  Wants=network-online.target
  After=network-online.target

  [Service]
  Type=simple
  ExecReload=/bin/kill -HUP $MAINPID
  ExecStart=/usr/bin/semaphore server --config /etc/semaphore/config.json
  SyslogIdentifier=semaphore
  Restart=always

  [Install]
  WantedBy=multi-user.target
  ```

2. **Copy your configuration file to the created directory:**
  ```sh
  sudo cp /root/config.json /etc/semaphore/config.json
  ```

3. **Stop running instances of Semaphore:**
  ```sh
  sudo pkill semaphore
  ```

4. **Confirm no Semaphore instances are running:**
  ```sh
  ps aux | grep sema
  ```

5. **Reload the systemd manager configuration:**
  ```sh
  sudo systemctl daemon-reload
  ```

6. **Start Semaphore service:**
  ```sh
  sudo systemctl start semaphore
  ```

7. **Check the status of Semaphore service:**
  ```sh
  systemctl status semaphore
  ```

8. **Enable Semaphore service to start on boot:**
  ```sh
  sudo systemctl enable semaphore
  ```

9. **Verify Semaphore is listening on port 3000**
  ```sh
  sudo ss -tunelp | grep 3000
  ```

10. **Access Semaphore:**
  Open your browser and navigate to `https://{{ localhost_IP }}:3000`
