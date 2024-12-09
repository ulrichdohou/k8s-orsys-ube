# Docker Installation Guide on Ubuntu

This guide provides step-by-step instructions to install Docker Engine on an Ubuntu system using `apt`.

---

## Prerequisites

- A 64-bit Ubuntu system compatible with one of the following versions:
  - Ubuntu 24.10 (Oracular)
  - Ubuntu 24.04 (Noble)
  - Ubuntu 22.04 (Jammy)
  - Ubuntu 20.04 (Focal)
- `sudo` privileges
- Active internet connection

---

## Installation Steps

### 1. Uninstall old versions of Docker

Remove any older versions of Docker if installed:
```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

### 2. Update package information

Update the `apt` package index:
```bash
sudo apt-get update
```

### 3. Install required packages

Install packages that allow `apt` to use a repository over HTTPS:
```bash
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

### 4. Add Docker’s official GPG key

Add the official GPG key for Docker:
```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### 5. Set up the Docker repository

Add Docker’s repository to `apt` sources:
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 6. Update package index

Update the package index to include the Docker repository:
```bash
sudo apt-get update
```

### 7. Install Docker Engine

Install Docker Engine, CLI, and Containerd:
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

### 8. Verify the installation

Run the Docker "hello-world" test image to verify the installation:
```bash
sudo docker run hello-world
```

---

## Post-installation (Optional)

### 9. Manage Docker as a non-root user

To run Docker commands without `sudo`:

- Create the `docker` group:
  ```bash
  sudo groupadd docker
  ```
- Add your user to the `docker` group:
  ```bash
  sudo usermod -aG docker $USER
  ```
- Log out and back in to apply the changes.

---

## Notes

- For additional details and advanced configurations, refer to the official Docker documentation for [Ubuntu](https://docs.docker.com/engine/install/ubuntu/) and the [post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/).
- Ensure your system is updated and you have the necessary privileges to install packages.

---

Happy containerization with Docker! 🚀