"""Check printed equation and rounded Figure4 slopes; not an isochron refit."""
import math,json
from pathlib import Path
sites=[('Topock',2.39,2.12,.26),('Bat Cave',2.47,2.05,.31),('Santa Fe Railway',.79,4.37,.71),('Palo Verde',1.63,3.04,.34)]
r={'source_id':'S216','locator':'printed56 equation5; printed59 Figure4, both visually inspected','tau_Ma':2.07,'nominal_initial_ratio':6.75,'equation_as_printed':'t = tau * ln(R_measured/R_initial)','decay_consistent_equation':'t = tau * ln(R_initial/R_measured)','assumptions':'Approximate tau and rounded slopes; no erosion correction, fit, covariance or age-uncertainty reproduction.','sites':[]}
for name,m,age,err in sites:
 literal=2.07*math.log(m/6.75)
 r['sites'].append({'site':name,'figure_slope':m,'figure_age_Ma':age,'figure_one_sigma_Ma':err,'literal_printed_equation_Ma':literal,'decay_consistent_nominal_age_Ma':-literal,'implied_initial_ratio_for_figure_age':m*math.exp(age/2.07),'interpretation':'Implied ratio is diagnostic back-calculation, not independently recovered correction.'})
Path('data/burial-slope-age-check.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
for s in r['sites']:print(s)
