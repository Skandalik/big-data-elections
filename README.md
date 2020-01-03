# big-data-elections
Project for Big Data class thats used for processing tweets and plotting charts.

### Important
All paths are defined in Windows-way. No support for OS X or Linux

### Requirements
* Docker and docker-compose installed
* Python and PiP installed
* Install requirements `pip install -r requirements.txt`

### Run
- `docker-compose up -d`
- `docker-compose up -d`
- `python main.py process` - normalize with defined path
  - `--filepath` - argument to provide filepath to scan and normalize data from. By default it points to `testdata`
  - `--batch` - batch size for saving after decompression. By default it's set for 10.
- `python main.py plot` - plot graphs