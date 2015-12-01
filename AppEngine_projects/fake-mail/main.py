import jinja2
import webapp2

env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class Email(object):
    def __init__(self, club_num, org_name,advisor_name,launched,email_address):
        self.club_num=club_num
        self.org_name=org_name
        self.advisor_name=advisor_name
        self.launched=launched
        self.email_address=email_address

class MainHandler(webapp2.RequestHandler):
    emails = [
  {
    "club_num": "C-000002377",
    "org_name": "San Carlos MasterCard Club",
    "advisor_name": "Kacee Bui",
    "advisor_email": "kacee_bui@mastercard.com",
    "launched": True,
    "Launch Date": "11/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000000816",
    "org_name": "San Pablo Community Center",
    "advisor_name": "Andrea Mendez",
    "advisor_email": "andream@sanpabloca.gov",
    "launched": True,
    "Launch Date": "8/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000000854",
    "org_name": "Teach School",
    "advisor_name": "Janet Crabb",
    "advisor_email": "jcrabb@slcusd.org",
    "launched": True,
    "Launch Date": "4/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000000868",
    "org_name": "Hercules Public Library",
    "advisor_name": "Michelle Ng",
    "advisor_email": "mng@ccclib.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000000876",
    "org_name": "Head-Royce School",
    "advisor_name": "Neethi Venkateswaran",
    "advisor_email": "nvenkateswaran@headroyce.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001141",
    "org_name": "Menifee Valley Middle School",
    "advisor_name": "Theresa Ladd",
    "advisor_email": "pcterrilynn@yahoo.com",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001232",
    "org_name": "Pacoima Middle School",
    "advisor_name": "Jennifer Bankston",
    "advisor_email": "jennylbee@gmail.com",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001247",
    "org_name": "Pacific Collegiate School",
    "advisor_name": "Trung Lai",
    "advisor_email": "trung.lai@pcsed.org",
    "launched": True,
    "Launch Date": "10/14/2015",
    "Volunteer Status": "Staffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001344",
    "org_name": "Caliber Beta Academy",
    "advisor_name": "Annie Patton",
    "advisor_email": "apatton@caliberbetaacademy.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001401",
    "org_name": "San Diego County Library - Encinitas Branch",
    "advisor_name": "Regine Thorne",
    "advisor_email": "regine.thorne@sdcounty.ca.gov",
    "launched": True,
    "Launch Date": "9/29/2015",
    "Volunteer Status": "Staffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001509",
    "org_name": "Belvedere Tiburon Library",
    "advisor_name": "Ivan Silva",
    "advisor_email": "isilva@beltiblibrary.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001783",
    "org_name": "Hillsdale High Schools",
    "advisor_name": "Debra Stucke",
    "advisor_email": "dstucke@smuhsd.org",
    "launched": True,
    "Launch Date": "8/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001807",
    "org_name": "Ardent Academy for Gifted Youth",
    "advisor_name": "James Li",
    "advisor_email": "dr.li@ardentacademy.com",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001813",
    "org_name": "Manchester Gate Elementary",
    "advisor_name": "Anita Ullner",
    "advisor_email": "anita.ullner@fresnounified.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001883",
    "org_name": "Milpitas High School",
    "advisor_name": "Jennifer Brady",
    "advisor_email": "jbrady@musd.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001954",
    "org_name": "Newbury Park High School",
    "advisor_name": "Richard Kick",
    "advisor_email": "rkick@conejousd.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001957",
    "org_name": "Gateway High School",
    "advisor_name": "Marc Crown",
    "advisor_email": "mcrown@gatewayhigh.org",
    "launched": True,
    "Launch Date": "10/12/2015",
    "Volunteer Status": "Full",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000001999",
    "org_name": "Northside Library (Santa Clara City)",
    "advisor_name": "Angela Ocana",
    "advisor_email": "aocana@santaclaraca.gov",
    "launched": False,
    "Launch Date": "12/1/2015",
    "Volunteer Status": "Staffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002003",
    "org_name": "Academy of Our Lady of Peace",
    "advisor_name": "Chris Boyer",
    "advisor_email": "cboyer@aolp.org",
    "launched": True,
    "Launch Date": "8/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002007",
    "org_name": "BASIS Independent Silicon Valley",
    "advisor_name": "Alexis Jefferson",
    "advisor_email": "alexis.jefferson@basisindependent.com",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002032",
    "org_name": "KIPP King Collegiate High School",
    "advisor_name": "Hari Vasu Devan",
    "advisor_email": "hari.vasu-devan@kippking.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002042",
    "org_name": "San Domenico School",
    "advisor_name": "Michael Sloan",
    "advisor_email": "msloan@sandomenico.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002071",
    "org_name": "Homestead High School",
    "advisor_name": "Amity Bateman",
    "advisor_email": "amity.bateman@gmail.com",
    "launched": True,
    "Launch Date": "10/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002078",
    "org_name": "St.Ignatius College Prep",
    "advisor_name": "Jennifer Gaspar-Santos",
    "advisor_email": "jsantos@siprep.org",
    "launched": True,
    "Launch Date": "10/1/2015",
    "Volunteer Status": "Staffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002083",
    "org_name": "Arroyo Seco Junior High School",
    "advisor_name": "Courtney Koegle",
    "advisor_email": "ckoegle@hartdistrict.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002087",
    "org_name": "San Francisco University High School",
    "advisor_name": "Byron Philhour",
    "advisor_email": "byron.philhour@sfuhs.org",
    "launched": True,
    "Launch Date": "10/6/2015",
    "Volunteer Status": "Full",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002113",
    "org_name": "La Crescenta Library",
    "advisor_name": "Marta Wiggins",
    "advisor_email": "mwiggins@library.lacounty.gov",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002129",
    "org_name": "Santa Clara high school",
    "advisor_name": "Rupali Satija",
    "advisor_email": "rsatija@scusd.net",
    "launched": True,
    "Launch Date": "10/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002135",
    "org_name": "Millbrae Library",
    "advisor_name": "Darren Heiber",
    "advisor_email": "heiber@smcl.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002137",
    "org_name": "St. Lucy's Priory High School",
    "advisor_name": "Victoria Hodge",
    "advisor_email": "vhodge@stlucys.com",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002140",
    "org_name": "Independence High School",
    "advisor_name": "Ellen Westlake",
    "advisor_email": "westlakee@esuhsd.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002141",
    "org_name": "Miramonte High School",
    "advisor_name": "Cindy Boyko",
    "advisor_email": "cindy.boyko@auhsdschools.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002147",
    "org_name": "American High School",
    "advisor_name": "John Holcomb",
    "advisor_email": "jholcomb@fremont.k12.ca.us",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002155",
    "org_name": "Fremont Main Library",
    "advisor_name": "Beth Ebuchanan",
    "advisor_email": "ebuchanan@aclibrary.org",
    "launched": False,
    "Launch Date": "1/1/2016",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002167",
    "org_name": "Leadership Public Schools Hayward",
    "advisor_name": "Laura Holguin",
    "advisor_email": "lholguin@leadps.org",
    "launched": True,
    "Launch Date": "10/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002177",
    "org_name": "Ardenwood School",
    "advisor_name": "Antoinette Schlobohm",
    "advisor_email": "toni@schlobohms.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002180",
    "org_name": "Saratoga High School",
    "advisor_name": "Judith Heher",
    "advisor_email": "jheher@lgsuhsd.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Staffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002201",
    "org_name": "Dougherty Valley High School",
    "advisor_name": "Preet Dalziel",
    "advisor_email": "pdalziel@srvusd.net",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002205",
    "org_name": "Monte Vista High School",
    "advisor_name": "Bhupinder Anwar",
    "advisor_email": "montevistagwc@gmail.com",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002243",
    "org_name": "Sand Creek High School",
    "advisor_name": "Todd Matia",
    "advisor_email": "tmatia@d49.org",
    "launched": True,
    "Launch Date": "10/30/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002246",
    "org_name": "George Washington High School",
    "advisor_name": "John Hajel",
    "advisor_email": "hajelj@sfusd.edu",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002269",
    "org_name": "Jefferson Elementary School District",
    "advisor_name": "Heavenley Anoa'i",
    "advisor_email": "hanoai24@yahoo.com",
    "launched": False,
    "Launch Date": "2/1/2016",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002285",
    "org_name": "Convent of the Sacred Heart High School",
    "advisor_name": "Riaz Abdulla",
    "advisor_email": "riaz.abdulla@sacredsf.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002293",
    "org_name": "Piedmont High School",
    "advisor_name": "Nathan Mattix",
    "advisor_email": "nmattix@piedmont.k12.ca.us",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002307",
    "org_name": "Santa Barbara Junior High School",
    "advisor_name": "Marilyn Garza",
    "advisor_email": "mgarza@sbunified.org",
    "launched": True,
    "Launch Date": "9/1/2015",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002315",
    "org_name": "Quarry Lane School",
    "advisor_name": "John Rogosic",
    "advisor_email": "jrogosic@quarrylane.org",
    "launched": False,
    "Launch Date": "1/1/2016",
    "Volunteer Status": "Unstaffed",
    "Primary State/Province": "California"
  },
  {
    "club_num": "C-000002289",
    "org_name": "Denver Public Library: ideaLAB",
    "advisor_name": "Laura Turk",
    "advisor_email": "lturk@denverlibrary.org",
    "launched": False,
    "Launch Date": "11/1/2015",
    "Volunteer Status": "Staffed",
    "Primary State/Province": "Colorado"
  }
]


    def get(self):
        template = env.get_template('main.html')
        variables = {'emails':self.emails}
        self.response.write(template.render(variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
