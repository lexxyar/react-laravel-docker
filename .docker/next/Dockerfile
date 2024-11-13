FROM node:23-alpine3.19

ARG NEXTJS_FOLDER

# RUN npm install -g npm@latest

WORKDIR /app-next

# disable telemetry
RUN npx next telemetry disable

COPY ./$NEXTJS_FOLDER/package.json ./package.json
RUN npm i

COPY ./$NEXTJS_FOLDER .
RUN npm run build



EXPOSE 3000

# server.js is created by next build from the standalone output
# https://nextjs.org/docs/pages/api-reference/next-config-js/output
ENV HOSTNAME="0.0.0.0"

CMD ["npm", "start"]
# CMD ["npm", "run", "dev"]
