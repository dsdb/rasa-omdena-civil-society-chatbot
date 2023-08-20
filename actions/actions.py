
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
#*****************************************************************************************
# Omdena Civil Sociery specific chanegs 
#*****************************************************************************************
# Import packages
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
import requests
import random
import pdb
import os
from rasa_sdk.executor import CollectingDispatcher

#*****************************************************************************************
# Greet User 
class ActionCivilSocietyGreet(Action):
    def name(self) -> Text:
        return "action_civil_society_greet"     

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_name = tracker.get_slot("civil_society_user_name")

        if user_name:
            greeting = f"Hello, {user_name}! Welcome to Omdena Civil Society. How can I assist you today?"
        else:
            greeting = "Hello! Welcome to Omdena Civil Society. Can I know your name?"

        dispatcher.utter_message(text=greeting)
        return [SlotSet("civil_society_user_name", user_name)] 
#--------------------------------------------------------------------------------------------------------
# Omdena civil society specific
#Get Partner details
class ActionCivilSocietyGetPartners(Action):
    def name(self) -> Text:
        return "action_civil_society_get_partners"

    def civil_society_get_partners(self) -> Dict[str, List[str]]:
        # Read the Civil Society Partners from the text file and return them as a dictionary
        with open("actions\civil_society_partners.txt", "r") as file:
            lines = file.readlines()

        partners_by_category = {}
        current_category = None

        for line in lines:
            line = line.strip()
            if line:
                if line.startswith("-"):
                    # Partner name under the current category
                    if current_category is not None:
                        partners_by_category[current_category].append(line[1:].strip())
                else:
                    # New category
                    current_category = line
                    partners_by_category[current_category] = []

        return partners_by_category

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        civil_society_partners = self.civil_society_get_partners()

        # Check if there are any partners
        if civil_society_partners:
            response = "Omdena has collaborated with the following Civil Society Partners:\n"
            for category, partners in civil_society_partners.items():
                response += f"\n{category}:\n"
                response += "\n".join(partners) + "\n"
        else:
            response = "There are currently no Civil Society Partners associated with Omdena."

        # Set the value of the 'civil_society_partner' slot to the fetched data
        return [SlotSet("civil_society_partners", response)]

class ActionCivilSocietyBenefitsOfAIEnabled(Action):
    def name(self) -> Text:
        return "action_civil_society_benefits_of_ai_enabled"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Organizations can 10x their impact by becoming AI-enabled through the Omdena platform. The platform offers access to a global AI community and diverse AI talent from around the world."
        dispatcher.utter_message(text=response)
        return []

class ActionCivilSocietyOmdenaPlatformOffer(Action):
    def name(self) -> Text:
        return "action_civil_society_omdena_platform_offer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "The Omdena platform offers organizations a collaborative ecosystem for AI projects. It connects them with a global community of AI experts. Through this diverse talent pool, organizations can access valuable perspectives, knowledge, and skillsets needed to develop AI solutions tailored to their specific challenges."
        dispatcher.utter_message(text=response)
        return []

class ActionCivilSocietyCaseStudies(Action):
    def name(self) -> Text:
        return "action_civil_society_case_studies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Here are some case studies showcasing the impact of Omdena's AI-enabled solutions: \n\n Climate change: ...\n Mental health: ...\n AI Assisted Collaborative Mapping Tool: ..."
        dispatcher.utter_message(text=response)
        return []

class ActionCivilSocietyGetTestimonials(Action):
    def name(self) -> Text:
        return "action_civil_society_get_testimonials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Working with Omdena was a game-changer for organization. Their collaborative approach and access to diverse AI talent allowed us to tackle complex problems we couldn't solve on our own.\n\"- Jean Ayoub, International Social Service, CEO.\n\"The Omdena platform provided us with the AI expertise we needed to help tackle the devastating social and economic cost of road crashes. Amazing experts in AI, the projects brought deep expertise to measure the safety of the world's roads and save lives. Unique and valuable experience - Rob McInerney, CEP IRAP\""
        dispatcher.utter_message(text=response)
        return []


class ActionCivilSocietyOutlineKeySteps(Action):
    def name(self) -> Text:
        return "action_civil_society_outline_key_steps"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response =  '''
        "The path to becoming an AI-enabled NGO involves several essential steps:
        Discover:
        The first step is to identify the problems or challenges that the NGO aims to address using AI.
        Simultaneously, the NGO needs to explore available data sources relevant to the identified problems.
        Agile Development:
        An initial innovation project is crucial to test and experiment with AI solutions. This short-term project helps the NGO explore different approaches to problem-solving using AI.
        Productionize:
        After successful proof of concept, the AI solution is transitioned into production. It is made accessible and usable by stakeholders to start generating real value.
        Capacity Building:
        To sustain AI initiatives, the NGO embarks on a larger project focused on building internal capacities. This includes developing technical skills among staff members, fostering collaboration and communication within the organization, and promoting problem-solving capabilities" 
        '''
        dispatcher.utter_message(text=response)
        return []
 
class ActionCivilSocietyExplainWorkingWithOmdena(Action):
    def name(self) -> Text:
        return "action_civil_society_explain_working_with_omdena"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = '''
        "Omdena offers various ways to collaborate and work together, each tailored to specific outcomes:
        AI Innovation Challenge:  
        Through the AI Innovation Challenge, organizations can participate in collaborative projects with Omdena's diverse top talent teams. The outcome of this engagement is the development of AI models that address specific challenges. Each project involves 50 engineers contributing a total of 5000 hours of development time. 
        Top Talent Teams:
        For organizations seeking AI products and solutions, Omdena provides dedicated top talent teams comprising 1 to 5 skilled engineers. These teams represent the top 2% of Omdena's talent pool, ensuring high-quality work and innovative results
        Hiring:
        Omdena also serves as a platform for organizations to find their next hire(s). Around 85% of startups"
        '''
        dispatcher.utter_message(text=response)
        return []


class ActionCivilSocietyDescribeSuccessfulJourney(Action):
    def name(self) -> Text:
        return "action_civil_society_describe_successful_journey"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = '''
        "Over a span of 10 months, the World Resources Institute (WRI) embarked on a highly successful journey with Omdena, engaging in transformative AI innovation. The collaboration resulted in remarkable achievements, with significant impact and outcomes. 
        Key highlights of the journey with Omdena are as follows:
        Duration: The collaboration between WRI and Omdena lasted for 10 months, allowing for comprehensive and in-depth exploration of various AI-driven initiatives.
        Innovation Projects: Throughout the partnership, WRI and Omdena actively collaborated on five innovation projects. These projects aimed to tackle complex environmental and sustainability challenges using AI-driven solutions.
        Products Developed: The collective effort of WRI and Omdena's talented teams led to the development of three AI products. These products were designed to address specific environmental issues, providing valuable insights and data-driven solutions.
        Funding Secured: The successful outcomes of the innovation projects and the potential of the AI products attracted interest and support from various stakeholders. 
        Collaborators Involved: The journey witnessed the active involvement of more than 150 collaborators."
        '''
        dispatcher.utter_message(text=response)
        return []


class ActionCivilSocietyDescribeCollaborationUpskilling(Action):
    def name(self) -> Text:
        return "action_civil_society_describe_collaboration_upskilling"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = '''
        "Omdena and WRI's teams are working closely together to provide upskilling opportunities for WRI's internal staff. Through this collaboration, WRI's staff gains valuable skills in managing and executing real-world AI projects successfully. This partnership empowers WRI to leverage AI technologies effectively to address environmental and sustainability challenges."
        '''
        dispatcher.utter_message(text=response)
        return []
    

class ActionCivilSocietyDescribeCollaborationSuccess(Action):
    def name(self) -> Text:
        return "action_civil_society_describe_collaboration_success"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = '''
        "The collaboration between Omdena and WRI plays a crucial role in the successful execution of real-world AI projects. By giving WRI access to their knowledge base and tool partnerships, Omdena empowers WRI's teams with the necessary AI skills and resources. This ensures that AI projects are well-informed and guided by best practices."
        '''
        dispatcher.utter_message(text=response)
        return []
    
class ActionCivilSocietyContactOmdena(Action):
    def name(self) -> Text:
        return "action_civil_society_contact_omdena"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Omdena Civil Society can be contacted through their website https://omdena.com/civil-society"
        dispatcher.utter_message(text=response)
        return []
    
#Domain specific actions
class ActionCivilSocietyHumanRightsPartners(Action):
    def name(self) -> Text:
        return "action_civil_society_human_rights_partners"    
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = '''
        "Amnesty International is a global human rights organization that works to protect individuals and groups who are denied basic rights. Omdena and Amnesty International have collaborated on a number of projects, including the development of a tool to track human rights abuses in Syria."
        "Human Rights Watch is a non-profit organization that monitors and reports on human rights abuses around the world. Omdena and Human Rights Watch have collaborated on a number of projects, including the development of a tool to track the use of torture in the Democratic Republic of Congo."
        "The Carter Center is a non-partisan organization that works to advance human rights and democracy around the world. Omdena and The Carter Center have collaborated on a number of projects, including the development of a tool to monitor elections in Kenya."
        "The Open Society Foundations is a philanthropic organization that supports projects that promote democracy, human rights, and justice around the world. Omdena and The Open Society Foundations have collaborated on a number of projects, including the development of a tool to track hate speech online."
        '''
        "One example of Omdena's work in the field of human rights is its collaboration with Amnesty International to develop a tool to track human rights abuses in Syria. The tool, called the Syriatracker, uses AI to collect and analyze data from social media and other sources to identify and document human rights abuses in Syria. "
        '''
        "Omdena's collaborations with human rights organizations have helped to develop powerful AI-powered tools that can be used to protect human rights and promote social justice. These tools have the potential to make a significant impact on the lives of people around the world who are denied basic rights."
        '''        
        dispatcher.utter_message(text=response)
        return []
    
class ActionCivilSocietyEnvironmentalSustainabilityPartners(Action):
    def name(self) -> Text:
        return "action_civil_society_environmental_sustainability_partners"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = '''
        "The Nature Conservancy: Omdena and The Nature Conservancy collaborated on a project to develop an AI-powered tool to track deforestation in the Amazon rainforest. The tool uses satellite imagery and machine learning to identify areas of deforestation. This information is used to help The Nature Conservancy to protect the rainforest and its inhabitants."
        '''
        '''
        "The World Resources Institute: Omdena and WRI collaborated on a project to develop an AI-powered tool to track water pollution in India. The tool uses satellite imagery and machine learning to identify areas of water pollution. This information is used to help WRI to protect India's water resources."
        '''
        '''
        "The United Nations Environment Programme: Omdena and UNEP collaborated on a project to develop an AI-powered tool to track climate change. The tool uses satellite imagery and machine learning to identify areas that are most vulnerable to climate change. This information is used to help UNEP to develop strategies to mitigate the effects of climate change."
        '''
        dispatcher.utter_message(text=response)
        return []
    
class ActionCivilSocietyHealthcareAcessPartners(Action):
    def name(self) -> Text:
        return "action_civil_society_healthcare_access_partners"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = '''
        "Access to Maternal Care in Sub-Saharan Africa: Omdena collaborated with the African Medical and Research Foundation (AMREF) to develop an AI-powered tool to improve access to maternal care in sub-Saharan Africa. The tool uses data from mobile phones and other sources to identify pregnant women who are at risk of complications. This information is used to help AMREF to provide these women with the care they need."
        "AI-Powered Chatbot for Women's Mental Health Support: Omdena collaborated with the NGO Pratham to develop an AI-powered chatbot for women's mental health support. The chatbot uses natural language processing to provide women with support and resources for mental health. This information is used to help Pratham to provide more accessible mental health care to women in India"
        "Mitigating Implicit Biases in Healthcare: Omdena collaborated with the Mayo Clinic to develop an AI-powered tool to mitigate implicit biases in healthcare. The tool uses machine learning to identify and address biases in healthcare settings. This information is used to help the Mayo Clinic to provide more equitable care to all patients."
        '''
        dispatcher.utter_message(text=response)
        return []
    
class ActionCivilSocietyMarginalizedCommunitiesPartners(Action):
    def name(self) -> Text:
        return "action_civil_society_marginalized_communities_partners"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = '''
        "Pratham is an NGO that works to improve education in India. Omdena and Pratham have collaborated on a number of projects, including the development of an AI-powered chatbot for women's mental health support."
        "UNDP is the United Nations Development Programme. Omdena and UNDP have collaborated on a project to develop an AI-powered tool to track the Sustainable Development Goals (SDGs)."
        '''
        dispatcher.utter_message(text=response)
        return []   
        
class ActionCivilSocietyEducationOpportunitiesPartners(Action):
    def name(self) -> Text:
        return "action_civil_society_education_opportunities_partners"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = '''"Aga Khan Foundation: Omdena and Aga Khan Foundation have collaborated on a project to develop an AI-powered tool to identify and address learning gaps in children. The tool uses machine learning to analyze data from student assessments and identify areas where children need additional support. This information is used to help Aga Khan Foundation to provide more personalized learning experiences for children."
        '''
        '''"UNESCO: Omdena and UNESCO have collaborated on a project to develop an AI-powered tool to track the progress of the Sustainable Development Goals (SDGs) in education. The tool uses data from a variety of sources to track the progress of the SDGs in education and identify areas where more work is needed. This information is used to help UNESCO to advocate for policies that will help to achieve the SDGs in education."
        '''
        dispatcher.utter_message(text=response)
        return []
       
class ActionCivilSocietyGloabalIssuesPartners(Action):
    def name(self) -> Text:
        return "action_civil_society_global_issues_partners"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = '''
        "Education: Omdena is working with organizations to develop AI-powered tools that can help to improve access to education, identify and address learning gaps, and track the progress of the Sustainable Development Goals (SDGs) in education."
        "Healthcare: Omdena is working with organizations to develop AI-powered tools that can help to improve access to healthcare, mitigate implicit biases in healthcare, and track the spread of diseases."
        "Environment: Omdena is working with organizations to develop AI-powered tools that can help to track deforestation, water pollution, and climate change." 
        '''
        dispatcher.utter_message(text=response)
        return []