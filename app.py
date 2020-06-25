# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, Markup
from flask import render_template
from flask import request



# -- Initialization section --
app = Flask(__name__)



months = {
    '1990': '1990:' + '<BR><h2>Wrecking cranes began tearing down the Berlin Wall at the Brandenburg Gate (April 29)</h3>' + '<BR><img border="2" width="900" src="https://www.abc.net.au/news/image/9399574-3x2-940x627.jpg"</img>' + '<BR><BR><BR><h2>1,426 pilgrims trampled to death after a panic in a tunnel in Mecca, Saudi Arabia (July 2)</h2>'+ '<BR><img border="2" width="600" src="https://s1.nyt.com/timesmachine/pages/1/1990/07/03/793390_360W.png?quality=75&auto=webp&disable=upscale"</img>' + '<BR><BR><BR><h2>US deploys troops to Saudi Arabia beginning Operation Desert Shield (August 7)</h2>' + '<BR><img border="2" width="900" src="https://archive.defense.gov/dodcmsshare/photoessay/2010-07/hires_DF-ST-91-05287.jpg"' + '<BR><BR><BR><h3> Here are some links for extra information about these three topics:</h3>' + '<BR><p>1. https://www.history.com/this-day-in-history/bush-orders-operation-desert-shield' + '<BR><p>2. https:https://www.history.com/this-day-in-history/pilgrim-stampede-kills-1400' + '<BR><p>3. https://www.history.com/this-day-in-history/bush-orders-operation-desert-shield',
    '1991': '1991:' + '<BR><h2>The formal Prime Minister of India, Ragiv Gandhi, was killed (May 21)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><BR><BR><h2>Gulf War ends after Iraq sets a ceasefire following their retreat to Kuwait (February 28)</h2>' + '<BR><img border="2" width="600" src="https://static.history.state.gov/milestones/desert-storm.jpg"</img>' + '<BR><BR><BR><h2>U.S.S.R comes to a formal end (December 21)</h2>' + '<BR><img border="2" width="600" src="https://image.slidesharecdn.com/thecoldwartheend-140810212935-phpapp02/95/the-cold-war-the-end-1-638.jpg?cb=1407706236"</img>' + '<BR><BR><BR><h3> Here are some links for extra information about these three topics:</h3>' + '<BR><p>1. https://en.wikipedia.org/wiki/Assassination_of_Rajiv_Gandhi' + '<BR><p>2. https://history.state.gov/milestones/1989-1992/gulf-war#:~:text=The%20invasion%20of%20Kuwait%20led,Kuwait%20on%20February%2028%2C%201991.' + '<BR><p>3. https://www.history.com/this-day-in-history/bush-orders-operation-desert-shield',
    '1992': '1992:', 
    '1993': '1993:',
    '1994': '1994:',
    '1995': '1995:',
    '1996': '1996:',
    '1997': '1997:',
    '1998': '1998:',
    '1999': '1999:',
    '2000': '2000:',
    '2001': '2001:',
    '2002': '2002:',
    '2003': '2003:',
    '2004': '2004:',
    '2005': '2005:',
    '2006': '2006:',
    '2007': '2007:',
    '2007': '2008:',
    '2009': '2009:',
    '2010': '2010:',
    '2011': '2011:',
    '2012': '2012:' + '<BR><h2>The American Episcopal Church becomes the first to approve a rite for blessing gay marriages (July 10)</h2>' + '<BR><img border="2" width="900" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/St._John%27s_Episcopal_Church.JPG/220px-St._John%27s_Episcopal_Church.JPG "</img>' + '<BR><h2>Kim Jong-un is officially appointed Supreme Leader of North Korea and given the rank of Marshal in the Korean Peoples Army (July 18)</h2>' + '<BR><img border="2" width="900" src="https://m.hindustantimes.com/rf/image_size_444x250/HT/p2/2020/06/22/Pictures/meeting-workers-central-korean-leader-committee-political_c7585384-b449-11ea-b3b3-7b919605787e.jpg"</img>' + '<BR><h2>Scientists detect evidence of light from the universes first stars, predicted to have formed 500 million years after the big bang (November 1)</h2>' + '<BR><img border="2" width="900" src="https://astronomy.com/-/media/Images/News%20and%20Observing/News/2018/03/bluestar2.jpg?mw=600"</img>',
    '2013': '2013:' + '<BR><h2>Xi Jinping is named as the new President of the Peoples Republic of China (March 14)</h2>' + '<BR><img border="2" width="600" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Xi_Jinping_2019.jpg/220px-Xi_Jinping_2019.jpg"</img>' + '<BR><h2>Human stem cells are successfully cloned (May 16)</h2>' + '<BR><img border="2" width="600" src="https://scx2.b-cdn.net/gfx/news/2017/stemcell.jpg"</img>' + '<BR><h2>Detroit, Michigan, files for bankruptcy, becoming the largest US municipal bankruptcy ever at $18.5 billion (July 18)</h2>' + '<BR><img border="2" width="600" src="https://www.gannett-cdn.com/-mm-/a8829d106dd33b1e9ab268db3ac336c09c02baf1/c=0-363-5184-3287/local/-/media/USATODAY/USATODAY/2013/12/03//1386049502000-AP-Detroit-Bankruptcy.jpg?width=660&height=373&fit=crop&format=pjpg&auto=webp"</img>' + '<BR><BR><BR><h3> Here are some links for extra information about these three topics:</h3>' + '<BR><p>1. https://www.bbc.com/news/world-asia-pacific-11551399' + '<BR><p>2. https://www.theverge.com/2013/5/15/4334670/first-cloned-human-embryonic-stem-cells' + '<BR><p>3. https://www.nytimes.com/2013/07/19/us/detroit-files-for-bankruptcy.html',
    '2014': '2014:' + '<BR><h2>Ukrainian Revolution of 2014 begins as protesters, riot police and unknown shooters take part in violent events in the capital, Kiev, culminating after five days in the ouster of President Viktor Yanukovych (February 18)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Islamic State of Iraq forces seize control of government offices and other important buildings in the northern city of Mosul (June 11)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Malaysia Airlines Flight 17 is shot down over Eastern Ukraine by a Buk surface-to-air missile launched from pro-Russian separatist-controlled territory, killing all 283 passengers and 15 crew on board (July 17)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><BR><BR><h3> Here are some links for extra information about these three topics:</h3>' + '<BR><p>1.' + '<BR><p>2. ' + '<BR><p>3. ',
    '2015': '2015:' + '<BR><h2>US scientists from University of California find evidence life on earth may have begun 4.1 billion years ago, 300 million earlier than previously thought (October 19)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Queen Elizabeth II becomes Great Britains longest-reigning monarch at 63 years and seven months, beating the previous record set by her great-great-grandmother, Queen Victoria (September 9)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>China announces the end of their one-child policy after 35 years (October 29)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><BR><BR><h3> Here are some links for extra information about these three topics:</h3>' + '<BR><p>1.' + '<BR><p>2. ' + '<BR><p>3. ',
    '2016': '2016:' + '<BR><h2>Panama Canals third set of locks opens for commercial traffic, doubling the Canals capacity at an estimated cost of $5.25 billion (June 26)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Brexit referendum: United Kingdom votes to leave the European Union (June 23)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Republican Donald Trump is elected President of the United States of America, defeating democrat Hillary Clinton, who received 2.9 million more votes (November 8)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><BR><BR><h3> Here are some links for extra information about these three topics:</h3>' + '<BR><p>1.' + '<BR><p>2. ' + '<BR><p>3. ',
    '2017': '2017:' + '<BR><h2>North Korea tests first successful intercontinental ballistic missile into Sea of Japan (July 4)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Hurricane Irma becomes the most powerful hurricane ever recorded in the Atlantic Basin region with winds of 185mph (280km/h) (September 5)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Islamic State headquarters Raqqa declared under full control of US-led alliance by Syrian Democratic Forces (SDF) spokesman Talal Sello after 4 months of fighting (October 17)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><BR><BR><h3> Here are some links for extra information about these three topics:</h3>' + '<BR><p>1.' + '<BR><p>2. ' + '<BR><p>3. ',
    '2018': '2018:' + '<BR><h2>Historic win in Malaysian general election by opposition coalition Pakatan Harapan led by 92 year old former Prime Minister Dr. Mahathir bin Mohamad, defeating Prime Minister Najib Razak and ending 61 years of rule by the Barisan Nasional coalition (May 9)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Apple becomes the first American public listed company to reach $1 trillion in value (August 2)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Indian Prime Minister Narendra Modi launches Modicare, free healthcare for 500 million, worlds biggest healthcare program (September 23)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><BR><BR><h3> Here are some links for extra information about these three topics:</h3>' + '<BR><p>1.' + '<BR><p>2. ' + '<BR><p>3. ',
    '2019': '2019:' + '<BR><h2>Global warming is the fastest in 2,000 years and scientific consensus that humans are the cause is at 99%, according to three major reports published in journals "Nature" and "Nature Geoscience" (July 24)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Sumatran rhino officially declared extinct in Malaysia after last known specimen, 25-year-old Iman, dies of cancer in Sabah, Malaysian Borneo (November 23)</h2>' +  '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>US House of Representatives votes to impeach President Donald Trump for abuse of power (230-197) and obstruction of Congress (229-198) (December 18)</h2>' +  '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' '<BR><BR><BR><h3> Here are some links for extra information about these three topics:</h3>' + '<BR><p>1.' + '<BR><p>2. ' + '<BR><p>3. ',
    '2020': '2020:' + '<BR><h2>Queen Elizabeth II issues a statement saying she reluctantly supports Prince Harry and Meghan Markles wish to live a more independent life (January 13)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Impeachment trial of US President Donald Trump begins in the Senate (January 16)' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><h2>Coronavirus COVID-19 declared a pandemic by the head of the World Health Organization Tedros Adhanom Ghebreyesus, with 121,564 cases worldwide and 4,373 death (March 11)</h2>' + '<BR><img border="2" width="600" src="https://cdn.dnaindia.com/sites/default/files/styles/full/public/2020/05/21/906813-rajiv-gandhi-new.jpg"</img>' + '<BR><BR><BR><h3> Here are some links for extra information about these three topics:</h3>' + '<BR><p>1.' + '<BR><p>2. ' + '<BR><p>3. ',

}



# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/sendMonth", methods=['GET', 'POST'])
def sendMonth():
    birth_month = request.form['month']
    birth_stone = months[birth_month]
    print(birth_stone)
    return render_template('results.html', stone=Markup(birth_stone))


