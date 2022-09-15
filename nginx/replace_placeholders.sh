#!/usr/bin/env sh

set -eu
envsubst '$PATH_LABEL $QUERY_LABEL' < /etc/nginx/conf.d/default.template > /etc/nginx/conf.d/default.template.conf
exec "$@"
