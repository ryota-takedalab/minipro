cd /home/r_tanaka/workspace6/venvs/py3venv/minipro

for %%f in (dataset/bvh-data/yusaku/*.bvh) do (
    bvh2csv -o dataset/csv-data/yusaku %%f
)