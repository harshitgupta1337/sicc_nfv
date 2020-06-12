#!/bin/bash
curl --header "Content-Type: application/json"   --request PUT   --data @sfc_1.json  http://localhost:8080/register_sfc
curl --header "Content-Type: application/json"   --request PUT   --data @sfc_2.json  http://localhost:8080/register_sfc
