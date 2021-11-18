# Kedro intermediate training

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/AntonyMilneQB/kedro-intermediate-training)

Last updated for kedro 0.17.5.

# Commands

## Modular pipeline

```bash
kedro pipeline pull ../data_filtering-0.1-py3-none-any.whl

kedro registry list
kedro registry describe filtered_pipeline

kedro pipeline package data_filtering
```
