## apartments-listing
### Apartments listing &amp; details application

### Four main components
- Database
- API
- Web app
- Mobile app

### For each
- infra/build.sh: builds image from Dockerfile
- infra/run.sh: runs container from an already built image

### build and run steps (implemented and tested on Ubuntu Jammy)
1.  cd /apartments
2.  sh ./db/infra/run.sh      # wait for 1 min for db to start
3.  sh ./api/infra/build.sh
4.  sh ./api/infra/run.sh
5.  sh ./prep_db.sh
6.  sh ./web/infra/build.sh
7.  sh ./web/infra/run.sh


### API Docs (assuming host == localhost):

add apartment with json post request body | /app/apartments - \[POST\]

curl --request POST --url http://127.0.0.1:8000/app/apartments --data '{"number": 33, "floor":44, "building":22, "city":"Cairo", "area_m2":200, "price":4444.44, "description": "nice one"}'

---
get all apartments | /app/apartments - \[GET\]

curl --request POST --url http://127.0.0.1:8000/app/apartments

---
get a single apartment - apartments/1 | /app/apartments/\<apartment-id\> - \[GET\]

curl --request POST --url http://127.0.0.1:8000/app/apartments/1

---

#### Mobile App
- The app uses a WebView component \(react-native-webview\) to implement the interface
- All code is within App.tsx
- This strategy was followed to take advantage from the React web app already implemented
- To run successfully run it, change the IP address in the WebView component to the WLAN IP of the connected machine
- This will allow it to connect to the React app hosted on the machine

#### Steps to run on device
1. cd apartments/
2. Run sh ./mobile/infra/build.sh
3. Run sh ./mobile/infra/run.sh          #you'll be directed to a shell session within the container
4. Connect your device via USB
5. Check connection by running 'adb devices'
6. cd into the app's directory
7. run npm run android \(or IOS\)
8. run npm start
