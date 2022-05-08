rm -rf output
mkdir -p output/backend output/frontend
cd output/backend
mkdir controller dto mapper model service repository
cd ../frontend
mkdir components models services 
cd ../..
cp -r static/* output
python3 script.py