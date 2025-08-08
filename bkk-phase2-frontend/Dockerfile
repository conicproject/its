# ✅ ใช้ image ที่เสถียรและรองรับ native module ได้ดี
FROM node:18-slim

# ✅ set working directory
WORKDIR /app

# ✅ add node_modules/.bin to PATH
ENV PATH /app/node_modules/.bin:$PATH

# ✅ install system dependencies
RUN apt-get update && apt-get install -y python3 make g++ git && rm -rf /var/lib/apt/lists/*

# ✅ copy package.json
COPY package.json ./

# ✅ install app dependencies
RUN npm install --force

# ✅ install vue-cli global พร้อม --unsafe-perm
RUN npm install @vue/cli@5.0.8 -g --unsafe-perm

# ✅ copy source files
COPY . .

# ✅ start app
CMD ["npm", "run", "serve", "--", "--host", "0.0.0.0"]
