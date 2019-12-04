exemplaire='./exemplaires/MTG_10_10'
solution='./tmp/sol_10_10'
bash tp.sh -e $exemplaire > $solution
python3 ./sol_check.py $exemplaire $solution

