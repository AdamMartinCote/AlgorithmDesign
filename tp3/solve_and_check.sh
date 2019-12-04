#!/usr/bin/env bash

function check_exemplaire() {
    echo -e "Résultats pour MTG_$1: "
    bash tp.sh -e "./exemplaires/MTG_$1" >"./tmp/sol_$1"
    python3 ./sol_check.py "./exemplaires/MTG_$1" "./tmp/sol_$1"
    echo ""
}

exemplaires=(
    5_100
    10_10
    10_20
    10_40
    20_5
)

for exemplaire in "${exemplaires[@]}"; do
    check_exemplaire "$exemplaire"
done
