#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
randomSeed(analogRead(0)); // seed random number generator

int time = random(3000, 5001); // get random number between 3000 and 5000 for the 3-5 seconds

// set up the LCD’s number of columns and rows:
lcd.begin(16, 2);
// Print a message to the LCD.
lcd.print("Welcome!");


delay(time); // wait for the 2 to 4 seconds

// set up the LCD’s number of columns and rows:
lcd.begin(16, 2);
// Print a message to the LCD.
lcd.print("Units : 400kWh ");
}

void loop() {
// set the cursor to column 0, line 1
// (note: line 1 is the second row, since counting begins with 0):
lcd.setCursor(0, 1);
// print a message to the lcd.
lcd.print("Amount: 381.45 RS "); 
}
