sudo systemctl start mongod

cd database
./build.sh
cd ..



cd mlmodels || exit
sudo ./build.sh
cd ..

cd backend || exit
python3 main.py &
cd ..


./backend/examples/requests.sh

cd frontend/galeno || exit
npm start &
cd ..

echo "system is running"

