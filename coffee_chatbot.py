import random
import re

#Ta motiba kai oi antistoixes apantiseis
patterns_responses = [
    (r'hello|hi|hey', ["Hello!How can I help you today?", "Hi! Ready for some coffee tips?"]),
    (r'\D*([1-9][0-9]*|0)(\.[0-9]+)?°C\D*(temperature for)(.*)' , ["The perfect {2}{3} is 90.5°C.", "It is good for{3} to have a temperature of 90.5°C.", "90.5°C is the perfect {2}{3}."]),
    (r'(.*)water pressure(.*)' , ["Properly,{1} we need 9 bars of water pressure." , "The water pressure{1} should be 9 bars."]),
    (r'\D*(2[5-9]|3[0-5])ml(.*)amount(.*)' , ["{0}ml are the perfect ml{2}."]),
    (r'\D*(0|1[0-9]*|2[0-4]*|3[6-9]*|[4-9][0-9]*|2[0-9][0-9]*|3[0-9][0-9]*)ml(.*)amount(.*)' , ["{0}ml are not the ideal ml{2}. You need 25-35ml", "Typically{2} we need around 25-35ml."]), 
    (r'(.*)(coffee with the ice for)(.*)freddo espresso', ["For{2}freddo espresso you have to shake the {1} 6-8 seconds.", "It's good to shake the {1} 6-8 seconds for{2}freddo espresso."]),
    (r'\D*(6[0-4](\.[0-9]+)?|65([\.0]+)?)°C\D*foam milk(.*)' , ["{0}°C are the best for boiling the foam milk.", "With {0}°C you can boil the foam milk perfectly."]),
    (r'\D*((0|[1-5][0-9]*|6[6-9]*|[7-9][0-9]*|6[0-9][0-9]*)(\.[0-9]+)?)°C\D*(foam milk)(.*)', ["With {0}°C you cannot boil the foam milk right, for the best result boil it between 60-65°C.", "Prefer to boil the foam milk between 60-65°C, {0}°C is out of these bounds."]),
    (r'(.*)why(.*)doesn\'?t taste(.*)', ["One reason why{1}doesn't have{2} taste is the quality of the water.", "Machines have to be very clean so that{1}have{2} taste."]),
    (r'exit', ["If you have more questions in the future, feel free to ask. Have a great day!"])
    ]

def response(uInput):
    for pattern, responses in patterns_responses:
        #Xrisi synartisis re.match gia antistoixisi tou pattern me to input tou xristi agnowntas apo to input tou xristi tous xaraktires ". , !, ?, ,". To re.IGNORECASE den kanei diakrisi pezwn/kefalaiwn, etsi dieukolunetai i diadikasia tis antistoixisis
        match = re.match(pattern, uInput.rstrip(".!?,"), re.IGNORECASE)
        if match:
            #Epilogi mias tuxaias apantisis apo tis dia8esimes tou ka8e pattern
            r = random.choice(responses)
            #Xrisi methodou format gia antikatastasi twn timwn tis epistrefomenis pleiadas stin apantisi pou epilex8ike
            return r.format(*match.groups())
    return "I'm not sure I understand you fully."

if __name__ == "__main__":
    print("Welcome to the Coffee Chatbot! Ask me anything about coffee or say 'exit' to exit.")

    while True:
        uInput = input("You: ")

        if uInput == 'exit':
            print("ChatBot:", response(uInput))
            break

        print("ChatBot:", response(uInput))