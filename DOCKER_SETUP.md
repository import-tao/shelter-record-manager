# Docker Setup Guide

This guide will walk you through installing Docker and setting up the Animal Shelter Management System using Docker.

## Installing Docker

### Windows
1. **System Requirements**
   - Windows 10 64-bit: Pro, Enterprise, or Education (Build 16299 or later)
   - Enable Hyper-V and Containers Windows features

2. **Install Docker Desktop**
   - Download Docker Desktop from [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)
   - Run the installer (Docker Desktop Installer.exe)
   - Follow the installation wizard
   - Start Docker Desktop from the Windows Start menu
   - Wait for Docker Desktop to start (check the whale icon in taskbar)

### macOS
1. **System Requirements**
   - macOS 10.15 or newer (Catalina or newer)

2. **Install Docker Desktop**
   - Download Docker Desktop from [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-mac/)
   - Open the downloaded .dmg file
   - Drag Docker to Applications
   - Start Docker from Applications
   - Wait for Docker to start (check menu bar icon)

### Linux (Ubuntu)
1. **Update package index**
```bash
sudo apt-get update
```

2. **Install prerequisites**
```bash
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

3. **Add Docker's official GPG key**
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

4. **Set up stable repository**
```bash
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

5. **Install Docker Engine**
```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

6. **Install Docker Compose**
```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Verifying Installation

1. **Check Docker installation**
```bash
docker --version
docker-compose --version
```

2. **Test Docker**
```bash
docker run hello-world
```

## Setting Up the Application

1. **Clone the repository**
```bash
git clone https://github.com/import-tao/shelter-record-manager.git
cd shelter-record-manager
```

2. **Build and start the containers**
```bash
docker-compose up --build
```
This command will:
- Build the application image
- Start all services (web, database, Redis, Celery)
- Set up volumes for persistent data
- Configure networking between containers

3. **Create a superuser**
In a new terminal, run:
```bash
docker-compose exec web python manage.py createsuperuser --settings=shelter.settings.base_settings
```

4. **Access the application**
- Open your browser and go to http://localhost:8000
- Log in with your superuser credentials

## Common Docker Commands

- **Start containers in background**
```bash
docker-compose up -d
```

- **Stop containers**
```bash
docker-compose down
```

- **View logs**
```bash
docker-compose logs
# For specific service:
docker-compose logs web
```

- **Restart services**
```bash
docker-compose restart
# For specific service:
docker-compose restart web
```

- **Execute commands in container**
```bash
docker-compose exec web bash
```

## Troubleshooting

1. **Port conflicts**
   - If port 8000 is in use, modify the port mapping in docker-compose.yml
   - Change "8000:8000" to "8001:8000" (or any available port)

2. **Database connection issues**
   - Ensure the database container is running: `docker-compose ps`
   - Check database logs: `docker-compose logs db`
   - Wait a few seconds after starting containers for database initialization

3. **Permission issues**
   - On Linux, you might need to run docker commands with sudo
   - Or add your user to the docker group:
     ```bash
     sudo usermod -aG docker $USER
     ```

4. **Container won't start**
   - Check logs: `docker-compose logs`
   - Ensure all required files exist
   - Verify environment variables are set correctly

## Data Persistence

- Database data is stored in the postgres_data volume
- Media files are stored in the media_volume
- Static files are stored in the static_volume

To list volumes:
```bash
docker volume ls
```

## Updating the Application

1. **Pull latest changes**
```bash
git pull origin master
```

2. **Rebuild containers**
```bash
docker-compose down
docker-compose up --build
```

3. **Apply migrations**
```bash
docker-compose exec web python manage.py migrate --settings=shelter.settings.base_settings
```

## Security Notes

- Change default database credentials in production
- Use proper SSL/TLS certificates
- Set secure environment variables
- Regular security updates for base images
- Monitor container logs for suspicious activity 