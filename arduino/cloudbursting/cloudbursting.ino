//Cloudbursting by Johann Diedrick

int inputPinValue;

void setup(){
 pinMode(A0, INPUT);
 Serial.begin(9600);
}


void loop(){
  inputPinValue = analogRead(A0);
  Serial.write(inputPinValue);
}

