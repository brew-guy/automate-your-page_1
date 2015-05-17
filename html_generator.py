# This file contains the submission material for the Udacity Nanodegree
# Introduction to Programming by Jes H.
#
# Written for Python 3.4.3
#
# Takes a list of concepts (each of which is itself a list) and will return
# the appropriate string of HTML. The HTML structure returned differs a bit
# from the course example as I enclose the concept_title in <h3></h3> instead
# of in <div class="concept-title"></div>.

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <h3>''' + concept_title + '''</h3>'''
    html_text_2 = '''
    <div class="concept-description">
        <p>
            ''' + concept_description + '''
        </p>'''
    html_text_3 = '''
    </div>
</div>'''

    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    title = concept[0]
    description = concept[1]
    return generate_concept_HTML(title, description)


EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]


def make_HTML_for_many_concepts(list_of_concepts):
    # Code that generates the appropriate HTML for a list of concepts.
    appended_HTML = ""
    for concept in list_of_concepts:
         appended_HTML += make_HTML(concept)
    return appended_HTML


print(make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS))
