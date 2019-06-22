# Electronic Ablation Station
This implementation is an adaptation of the implementation suggested in the paper
[Open-source Automatic Weather Station and Electronic Ablation Station for measuring the impacts of climate change on glaciers](https://www.researchgate.net/publication/330195239_Open-source_Automatic_Weather_Station_and_Electronic_Ablation_Station_for_measuring_the_impacts_of_climate_change_on_glaciers)

The one thing that I did differently was instead of using RFID sensors and RFID tag to measure the change in the level of the glacier, I used metallic strip (e.g. aluminium foil) on a PVC rod each strip 1 inch apart. Inside the setup I have used two other aluminimum strip (a substitute of carbon brush). As ice melts, the setup goes downward. At one point of time circuit completes as two metallic strip touch the metallic strip on the PVC rod. When circuit completes then temperature and humidity are recorded along with the timestamp. Number of entry recorded denotes number of inches glacier has melted. The advantage of using metallic strip instead of RFID sensor and tags is that it can measure upto any resolution i.e. if we want to measure the change in the glacier in milimeter or centimeter range then that is also possible by changing the spacing between the metallic strips on the PVC rod. But this is not possible in case of RFID tags because if two tags are close enough then RFID sensor will get confused which one to read. 



<img src="images/1.jpeg" height="450" width="300">
Two metallic strips are attached on the top from inside of the box. These two metallic strips on the top complete the circuit when PVC rod slide through it (due to melting of glacier) and touches the metallic strip on the PVC rod.
 
 
 
 
 
<img src="images/2.jpeg" height="450" width="300">
Raspberry pi with DTH11 sensor to capture humidity and temperature





<img src="images/3.jpeg" height="450" width="300">
Two metallic strip which will be attached on top of the setup





<img src="images/4.jpeg" height="450" width="300">
PVC rod with metallic strip some fixed distance apart
