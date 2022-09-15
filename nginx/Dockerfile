# ### STAGE 1: Build ###
# FROM registry.access.redhat.com/ubi8/nodejs-14:1-51 as build-deps
# #WORKDIR /usr/src/app

# WORKDIR /app
# USER 0
# COPY package-lock.json ./
# COPY package.json ./
# RUN npm ci
# COPY . .
# RUN npm run build

### STAGE 2: Run ###
FROM registry.access.redhat.com/ubi8/nginx-118:1-46 as final

USER 0
WORKDIR /usr/share/nginx/html

COPY default.conf /etc/nginx/conf.d/default.template
COPY nginx.conf /etc/nginx/nginx.conf
COPY replace_placeholders.sh /
COPY dist /usr/share/nginx/html
# EXPOSE 8080

ENTRYPOINT [ "sh", "/replace_placeholders.sh" ]

RUN chown -R 1001:0 /etc/nginx && \
    chown -R 1001:0 /usr/share/nginx/html

USER 1001
CMD ["nginx",  "-g", "daemon off;"]


######################################################
#FROM registry.access.redhat.com/ubi8/nodejs-14:1-51 as build-deps
#LABEL maintainer="GpnDs"
#
#WORKDIR /app
#USER 0
#
#COPY package-lock.json ./
#COPY package.json ./
## install dependencies
#RUN npm ci
#COPY ./ .
#RUN npm run build
## copy source files
#
#
#
#
## Stage 2 - the production environment
#FROM registry.access.redhat.com/ubi8/nginx-118:1-46 as final
#ARG APP_VERSION
#LABEL maintainer="GpnDs"
#EXPOSE 8080
#
#USER 0
#WORKDIR /usr/share/nginx/html
#
### copy app files
#COPY default.conf /etc/nginx/conf.d/default.template
#COPY nginx.conf /etc/nginx/nginx.conf
#COPY replace_placeholders.sh /
#COPY --from=build-deps /app/dist /usr/share/nginx/html
#
#RUN ["chmod", "+x", "/replace_placeholders.sh"]
#ENTRYPOINT ["/replace_placeholders.sh"]
#
### add permissions for 1001
#RUN chown -R 1001:0 /etc/nginx && \
#    chown -R 1001:0 /usr/share/nginx/html
#
#USER 1001
#CMD nginx -g "daemon off;"
