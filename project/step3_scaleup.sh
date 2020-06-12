#!/bin/bash
curl --header "Content-Type: application/json"   --request PUT   --data @scale_sfc_1.json  http://localhost:8080/launch_sfc
curl --header "Content-Type: application/json"   --request PUT   --data @scale_sfc_2.json  http://localhost:8080/launch_sfc
