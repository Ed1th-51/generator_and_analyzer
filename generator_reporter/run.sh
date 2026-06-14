#!/bin/bash

case $1 in
    build_generator)
        docker build -t generator_app ./part_of_creating
    ;;
    run_generator)
        docker run -v ./data:/data generator_app
    ;; 
    create_local_data)
        docker run -v ./local_data:/data generator_app
    ;;
    build_reporter)
        docker build -t reporter_app ./part_of_analytics
    ;;
    run_reporter)
        docker run -v ./data:/data reporter_app
    ;;
    clear_data)
        rm data/data.csv
        rm data/report.html
    ;;
    structure)
        ls -R
    ;;
esac