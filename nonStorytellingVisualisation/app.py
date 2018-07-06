# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

server = app.server # the Flask app

app.layout = html.Div(children=[
dcc.Markdown('''
# Lerarentekort primair onderwijs

In heel Nederland is er een tekort aan leraren voor het primair onderwijs. In 2018 gaat het volgens de Rijksoverheid om een tekort van 1824 full-time leraren en directeuren. Dit tekort komt voornamelijk door de hoge werkdruk en het relatief lage salaris. Door de snelle bevolkingsgroei is het probleem in de steden in de Randstad het grootst. Zo heeft Amsterdam volgend schooljaar een verwacht docententekort van 1.6% ([Rijksoverheid, 2018](https://www.rijksoverheid.nl/onderwerpen/werken-in-het-onderwijs/aanpak-tekort-aan-leraren/lerarentekort-primair-onderwijs.)).

De kaart hieronder laat met behulp van kleur zien hoe groot het verwachtte lerarentekort per regio in 2020 is. 

![Image](https://www.rijksoverheid.nl/binaries/medium/content/gallery/rijksoverheid/content-afbeeldingen/onderwerpen/werken-in-het-onderwijs/vacaturedruk-po-kaart.png)

## Gevolgen lerarentekort in 2018

Het kan voorkomen dat een leraar door bijv. ziekte onverhoopt niet voor zijn klas kan staan. Door het lerarentekort is er in dit geval helaas vaak geen vervangende docent beschikbaar. Daarom moet er gekozen worden voor oplossingen zoals het naar huis sturen van de klas of het laten doceren door een onbevoegde. Om de gevolgen van het probleem in kaart te brengen zijn dit soort situaties in 2018 door scholen bijgehouden. 

Klik op de onderstaande knop om deze gegevens te bekijken: 
''', className='container',
    containerProps={'style': {'maxWidth': '650px'}}),
    html.Div([
        html.A(html.Button('Ga naar statistieken'),
        href='https://lerarentekortisnu.nl/stat.php', target="_blank")
    ], className='container', style={'maxWidth': '650px'}),
    dcc.Markdown('''
## Toename tekort
Zoals duidelijk wordt uit deze statistieken zijn er nu al veel negatieve gevolgen van het lerarentekort. Er wordt echter voorspelt dat als we de huidige koers blijven varen het lerarentekort en de bijbehorende problemen alleen maar groter worden.

De verwachtingen zijn af te lezen in de onderstaande grafiek.
 
![Image](https://image.ibb.co/eYN8Ko/verwachte_tekorten_leraren_en_directeuren_po.png)
[Bron: Rijksoverheid 2018](https://www.rijksoverheid.nl/onderwerpen/werken-in-het-onderwijs/aanpak-tekort-aan-leraren/lerarentekort-primair-onderwijs)

Het lerarentekort wordt voornamelijk veroorzaakt door te weinig loon en een hoge werkdruk. Goed onderwijs is een van de pijlers van de samenleving en daarom is een betere CAO voor docenten in het primair onderwijs hard nodig!

''', className='container',
    containerProps={'style': {'maxWidth': '650px'}}),



])

app.css.append_css({
    'external_url': 'https://codepen.io/rens/pen/dKRZOo.css'
})

if __name__ == '__main__':
    app.run_server(debug=True, port=8060)