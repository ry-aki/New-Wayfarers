import pickle
cfile=open("D:\\THE NEW WAYFARERS\\Carrental.txt",'wb+') 
c1={'no':1,'car':'Baleno','model':'Premium Hatchback','fuel':'Petrol','mode':'Automatic'}
c2={'no':2,'car':'Celerio','model':'Mid-Size Hatchback','fuel':'Petrol','mode':'Automatic'}
c3={'no':3,'car':'Dzire','model':'Compact Sedan','fuel':'Petrol','mode':'Manual'}
c4={'no':4,'car':'Ertiga','model':'Mid-Size MUV','fuel':'Petrol','mode':'Automatic'}
c5={'no':5,'car':'Ignis','model':'Micro SUV','fuel':'Petrol','mode':'Manual'}
c6={'no':6,'car':'Vitara Brezza','model':'Compact SUV','fuel':'Petrol','mode':'Manual'}
c7={'no':7,'car':'Carnival','model':'Luxury MPV','fuel':'Diesel','mode':'Automatic'}
c8={'no':8,'car':'Swift','model':'Mid-Size Hatchback','fuel':'Petrol','mode':'Manual'}
c9={'no':9,'car':'Wagon-R','model':'Mid-Size Hatchback','fuel':'Petrol','mode':'Manual'}
c10={'no':10,'car':'Creta','model':'Mid-Size SUV','fuel':'Diesel','mode':'Automatic'}  
c11={'no':11,'car':'Elantra','model':'Executive Sedan','fuel':'Diesel','mode':'Manual'}
c12={'no':12,'car':'Santro','model':'Mid-Size Hatchback','fuel':'Petrol','mode':'Manual'}
c13={'no':13,'car':'Venue','model':'Compact SUV','fuel':'Diesel','mode':'Automatic'}
c14={'no':14,'car':'Elite i20','model':'Premium Hatchback','fuel':'Petrol','mode':'Automatic'}
c15={'no':15,'car':'Grand i10 Nios','model':'Mid-size Hatchback','fuel':'Petrol','mode':'Automatic'} 
c16={'no':16,'car':'Nexon','model':'Compact SUV','fuel':'Diesel','mode':'Manual'}  
c17={'no':17,'car':'Tiago','model':'Mid-Size Hatchback','fuel':'Petrol','mode':'Automatic'}  
c18={'no':18,'car':'Tigor','model':'Compact Sedan','fuel':'Petrol','mode':'Manual'}  
c19={'no':19,'car':'Amaze','model':'Compact Sedan','fuel':'Diesel','mode':'Manual'} 
c20={'no':20,'car':'City','model':'Mid-Size Sedan','fuel':'Diesel','mode':'Manual'}  
c21={'no':21,'car':'Jazz','model':'Premium Hatchback','fuel':'Petrol','mode':'Automatic'}  
c22={'no':22,'car':'Bolero','model':'Mid-Size SUV','fuel':'Diesel','mode':'Manual'}
c23={'no':23,'car':'Scorpio','model':'Mid-Size SUV','fuel':'Diesel','mode':'Manual'}
c24={'no':24,'car':'Thar','model':'Compact 4X4 SUV','fuel':'Petrol','mode':'Automatic'}  
c25={'no':25,'car':'EcoSport','model':'Compact SUV','fuel':'Diesel','mode':'Automatic'}  
c26={'no':26,'car':'Figo','model':'Mid-Size Hatchback','fuel':'Petrol','mode':'Manual'}  
c27={'no':27,'car':'Duster','model':'Mid-Size SUV','fuel':'Petrol','mode':'Automatic'}  
c28={'no':28,'car':'Vento','model':'Mid-Size Sedan','fuel':'Petrol','mode':'Automatic'}  
c29={'no':29,'car':'Rapid','model':'Mid-Size Sedan','fuel':'Petrol','mode':'Manual'} 
c30={'no':30,'car':'Urban Cruiser','model':'Compact SUV','fuel':'Petrol','mode':'Automatic'} 
pickle.dump(c1,cfile)
pickle.dump(c2,cfile)
pickle.dump(c3,cfile)
pickle.dump(c4,cfile)
pickle.dump(c5,cfile)
pickle.dump(c6,cfile)
pickle.dump(c7,cfile)
pickle.dump(c8,cfile)
pickle.dump(c9,cfile)
pickle.dump(c10,cfile)
pickle.dump(c11,cfile)
pickle.dump(c12,cfile)  
pickle.dump(c13,cfile)
pickle.dump(c14,cfile)
pickle.dump(c15,cfile)
pickle.dump(c16,cfile)
pickle.dump(c17,cfile)
pickle.dump(c18,cfile)
pickle.dump(c19,cfile)
pickle.dump(c20,cfile)
pickle.dump(c21,cfile)
pickle.dump(c22,cfile)
pickle.dump(c23,cfile)
pickle.dump(c24,cfile)
pickle.dump(c25,cfile)
pickle.dump(c26,cfile)
pickle.dump(c27,cfile)
pickle.dump(c28,cfile)
pickle.dump(c29,cfile)
pickle.dump(c30,cfile)
cfile.close()
C={}
Cfile=open("D:\\THE NEW WAYFARERS\\Carrental.txt",'rb')
try:
    while True:
        C=pickle.load(Cfile)
        print(C)
except EOFError:
    print('EOF reached')
    Cfile.close()














    
