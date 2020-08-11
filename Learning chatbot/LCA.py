#-*-coding:utf8;-*-

def euclidean_similarity(x,y):
    x,y = x.lower(),y.lower()
    a = set(x.split())
    b = set(y.split())
    c = float(len(a&b))
    d = float(len(a|b))
    try:similarity_ratio = round(((c/d)*100/1),2)
    except:similarity_ratio = 0
    return(similarity_ratio)


class Chatbot(object):
    """ an advanced chatbot class capable of learning a new response to an input its memory is a text file with the name
    of the chatbot as its name. it uses a simple algorithm which is called Learning Chatbot Algorithm(LCA) for short. which is a pretty much simple
    chatbot response selection and learning algorithm """
    
    def __init__(self,name,**kwargs):        
        """ name --> is the name which u chose your chatbot to answer
            user_data --> is a list comprising of both the user name and gender
            logging --> is a boolean True means save user/bot conversations False means otherwise
            read_only --> is a boolean True means don't learn any new response False means otherwise
            load_default --> is a boolean True means load default responses False otherwise """
        self.name = name
        self.read_only = kwargs.get("read_only",False)
        
        self.filex = open("LCA.txt","a+")
        # show learning mode
        if not self.read_only:
            print(self.name+" now in learning mode")
        else:
            if self.read_only: print (self.name+" now in read only mode")
            else: print(self.name+" now in learning mode")  
        
        #define some local variables
        self.threshold = 70
        self.temp_memory = []        
        self.response = None
        self.msg = "learning disable please enable learning by setting the read only flag to False"
        
        
    def learn_response_from(self,inputx,response):
        self.filex = open("LCA.txt","a+")
        self.filex.write(("%s\n%s\n"%(inputx,response)))
        self.filex.close()
           
    def Learner(self,input):
        """
        learns a new response if there is no response to an input 
        or returns an returns if there is one
        """
        self.response = None
        self.brain = [i.strip() for i in open("LCA.txt")]
        # are we allowed to learn new response
        if self.read_only:
            return self.msg
        # checks wether we are learning a new sentence
        elif len(self.temp_memory) == 1:
            self.temp_memory.append(input)
            sentence = self.temp_memory[0]
            response = self.temp_memory[1]
            if response != "":
                self.temp_memory = []
                self.learn_response_from(sentence,response)
                return(response)
            else:
                self.temp_memory = []
                return("discarded learning")
        # checks wether we already know the input parsed
        elif input in self.brain:
            pass
        # since we don't recognize the input we LEARN it
        else:
            self.temp_memory.append(input)
            return("%s ?"%"please what should be my response")
        
            
    def Generate_response(self,input,data_source):
        """
        Generates a list of responses for the LCA to choose from
        """     
        for id,text in enumerate (data_source):
            #print(text +"==="+ input,euclidean_similarity(text,input))
            if euclidean_similarity(text,input) >= self.threshold:
                try:
                    return(data_source[id+1])
                except:
                    return(data_source[id-1])
            
                  
    def is_learning(self,input):
        """
        checks wether the chatbot is supposed to learn a new response to an input
        returns True or False
        """
        self.brain = [i.strip() for i in open("LCA.txt")]
        if len(self.temp_memory) == 1:
            return True
        elif input in self.brain:
            return False
        elif self.Generate_response(input,self.brain) != None :
            return(False)
        else:
            return True
        
    def LCA(self,input):
        """
        the engine box of the entire program balances between learning and response generation
        """
        response = None
        self.brain = [i.strip() for i in open("LCA.txt")]
        
        if self.is_learning(input):
            return self.Learner(input)
        else:
            response = self.Generate_response(input,self.brain)
            if input == "":return("Null input")
            if input not in self.brain and self.read_only != True:
                if type(response) == list:
                    response = choice(response)
                    response = (len(self.brain)+1,response[1])
                    self.learn_response_from(input,response[1])
                else:
                    self.learn_response_from(input,response)
            else:pass
        return(response)
    
    
bot = Chatbot("pybot")#,read_only=True)

while 1:
    user = input("User: >> ")
    response = bot.LCA(user)
    print("Bot: >> %s"%response)
    
    
print([i.strip() for i in open("LCA.txt")])