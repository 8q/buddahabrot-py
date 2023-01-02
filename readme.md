# buddhabrot-py

```shell
$ ./calc.py -h
usage: calc.py [-h] processes

positional arguments:
  processes   number of cpu to use for calculation

options:
  -h, --help  show this help message and exit
  
$ ./draw.py -h     
usage: draw.py [-h] outfile

positional arguments:
  outfile     ex) out.png

options:
  -h, --help  show this help message and exit
```

```shell
$ pipenv sync
$ pipenv shell
$ ./calc.py 8 > out.txt
$ ./draw.py out.png < out.txt
```

#### MaxDepth=20
![out_20.png](sample%2Fout_20.png)

#### MaxDepth=100
![out_100.png](sample%2Fout_100.png)

#### MaxDepth=1000
![out_1000.png](sample%2Fout_1000.png)

#### MaxDepth=12345
![out_12345.png](sample%2Fout_12345.png)
