#!/bin/bash
# copy file to azure blob storage

az storage file upload-batch --destination        \
                             --source
#                             [--account-key]
#                             [--account-name]
#                             [--connection-string]
#                             [--content-cache-control]
#                             [--content-disposition]
#                             [--content-encoding]
#                             [--content-language]
#                             [--content-md5]
#                             [--content-type]
#                             [--destination-path]
#                             [--dryrun]
#                             [--max-connections]
#                             [--metadata]
#                             [--no-progress]
#                             [--pattern]
#                             [--sas-token]
#                             [--subscription]
#                             [--validate-content]
