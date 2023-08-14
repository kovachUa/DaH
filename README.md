Створти дериво каталогів.
data
│   ├── json
│   │   ├── repos
│   │   ├── site
│   │   └── youtube
│   └── mirror
│       ├── reposgit
│       ├── site
│       └── youtube
Фалйи теж потрібно створити
  httrack:
    build:
      context: .
      dockerfile: ./httrack/Dockerfile
    volumes:
      - ./data/mirror:/mirror:rw
      - ./data/json:/json:ro
Додавати посилання списком
