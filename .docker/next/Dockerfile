FROM node:alpine

ARG NEXTJS_FOLDER

WORKDIR /app-next
COPY ./$NEXTJS_FOLDER/package.json ./package.json
RUN npm i

COPY ./$NEXTJS_FOLDER .
RUN npm run build

EXPOSE 3000

# server.js is created by next build from the standalone output
# https://nextjs.org/docs/pages/api-reference/next-config-js/output
ENV HOSTNAME="0.0.0.0"
CMD ["npm", "start"]