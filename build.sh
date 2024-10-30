sudo systemctl start mongod

cd database
./build.sh
cd ..

cd backend || exit
python3 main.py &
cd ..

cd frontend/galeno || exit
npm start &
cd ..

echo "system is running"

