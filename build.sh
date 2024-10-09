sudo systemctl start mongod

cd database
./build.sh
cd ..


cd mlmodels
sudo ./build.sh
cd ..


cd mlmodels
sudo ./build.sh
cd ..

cd backend
python3 main.py
cd ..

cd backend/examples
./requests.sh
