# %% 
import re
# %%
latex = r'''
    Canopies comprising large arrays of rigid or flexible structures are ubiquitous throughout natural 
    environments, and instrumental in a range of engineering applications. Quantifying the distinct 
    fluid-structure interaction and changes in the structure of the flow within and around such canopies 
    is crucial to optimize processes at various spatial scales. In nature, aquatic vegetation canopies  
    strongly modulate flows \citep{gambi1990flume, chen2013flow}, attenuate waves 
    \citep{fonseca1992preliminary, paul2012wave}, and regulates the turbulence impacting sediment 
    transport, deposition \citep{lefebvre2010influence, ortiz2013mean}, 
    nutrient fluxes \citep{mcglathery2007eutrophication, lawson2012enhancement}, 
    and spore dispersion within agricultural crop fields \citep{mccartney1994dispersal}. 
    In engineering, canopies contribute to the mixing of scalars and fluxes [REF] and offer 
    the potential for energy harvesting via, e.g., piezoelectric devices \citep{bae2014flutter}, among others.
    A review of aquatic vegetation canopy flows by \citet{nepf2012flow} points out that while 
    the frontal area modulates the mean flow, characteristics turbulent length scales are set by 
    the stem width or diameter and spacing, and indicated the possible spatial and temporal flow 
    variability due to canopy oscillations. Quantification of the interaction between flow and 
    flexible canopies is a requirement in the understanding of the distinct processes over the 
    boundary layer above the canopy. 
    Flexible structures exposed to flows undergo reduced drag compared to a rigid counterpart
    \citep{vogel1984drag, gosselin2010drag}.  
    \cite{luhar2011flow} assessed the role of blade stiffness and 
    buoyancy on blade reconfiguration, and proposed a model for drag and extent 
    of reconfiguration, applicable to seagrass and microalgae in natural settings. 
    Their model defines the degree of reconfiguration as a function of the dimensionless 
    ratio of drag to stiffness restoring force (Cauchy number, $Ca$) and the ratio of the 
    restoring force due to buoyancy and the stiffness (buoyancy parameter, $B$), defined 
    as $Ca=\rho_f bl^{3}U^{2}/(EI)$ and $B= (\rho_f - \rho_v) gbdl^{3}/(EI)$, where
    $\rho_{f}$ and $\rho_{v}$ are the fluid and blade material densities,  $b$, $d$ and $l$ are 
    the width, thickness and length of each blade,  $U$  is the bulk incoming velocity, $E$ is 
    the Young Modulus, and  $I$  is the second moment of inertia \citep{luhar2016wave}. In addition 
    to the material properties, the blade geometry further alters the reconfiguration behavior 
    \citep{albayrak2012flow}, and the unsteady dynamics \citep{jin2018flow}.
    \citet{naudascher2017flow} discussed three mechanisms 
    of flow-induced motion (FIM) of flexible elements, namely, i) 
    an instability-induced excitation (IIE) due to a self-induced 
    flow instability, such as wake turbulence generated by vortex 
    shedding, including vortex-induced vibrations (VIVs), ii) an 
    extraneously-induced excitation (EIE) caused by incoming flow 
    fluctuations that develop independently from the plate, and iii) a 
    motion-induced excitation (MIE) that occurs as a result of changes 
    in the surrounding fluid forces due to the plate vibration. The motion 
    of flexible plates can result from one process or multiple FIM processes. 
    The frequency of VIV of a flexible structure usually corresponds to the 
    well-known Strouhal relationship, such that the frequency of vortex 
    shedding  $f_v= \frac{S_tU}{L}$, where  $S_t$  is the Strouhal number, 
    and $L$ is the blade length scale, which is the diameter in cylindrical structures.
    \citet{jin2018instability} noted a decoupling between the frequency of the natural 
    blade frequency and wake flow fluctuations; vortex shedding following the Strouhal 
    relationship may occur without inducing blade motion and reasoned this was due to the 
    dependence on blade stiffness. Characterization of such dynamics in flexible canopies 
    is currently limited.
    The presence of neighboring flexible plates may lead to distinct dynamics and flow, with 
    such interactions being dependent on the relative spacing and alignment of the structures.
    \citet{kim2010constructive} found that due to vortex shedding from an upstream flag, the 
    drag on a downstream structure either increased or decreased depending on the phase. 
    \citet{jin2018couple} inspected two plates in tandem, and noted that the motion of the 
    upstream plates was related to the natural blade frequency, whereas the oscillations of 
    the downstream body depended on the structure of the flow shed from the upstream plate. This 
    coupled effect is dependent on the separation between the blades, with the reduced coupling at 
    increased spacing. The motions of singular and tandem blades are instrumental in understanding 
    the flow-structure interaction in complex canopies.
    The dynamics of flexible plates within a canopy may result in distinct 
    flows. \citet{finnigan2000turbulence} presented a comprehensive review of 
    the flow dynamics and turbulence within terrestrial plant canopies. Canopy obstruction 
    and imposed drag cause an inflection point in the vertical profile of streamwise velocity, 
    leading to the formation of a shear layer susceptible to Kelvin-Helmholtz (KH) instability, 
    which may result in a mixing layer dominated by comparatively large coherent vortices 
    \cite{raupach1996coherent, ghisalberti2002mixing, nepf2012flow}.  \citet{okamoto2013spatial} 
    explored the transition of a boundary layer impinging a canopy into a fully-developed mixing layer 
    region dominated by coherent vortices further downstream. Coherent vortices can then result in canopy 
    motion, which has been categorized depending on the extent of the motions into negligible, 
    gently swaying, energetic coherent waving (\textit{monami}), and prone \citep{nepf2000flow}. 
    \citet{ghisalberti2006structure} linked canopy motion to the existence of sweep and ejection 
    events, which in turn influence the turbulence statistics and vertical mixing. 
    \citet{ghisalberti2006structure} highlighted significant interactions between 
    canopy motion and hydrodynamics, finding that canopy waving resulted in a substantial 
    decrease in turbulent momentum transfer through the shear layer. The dynamics of the plates 
    within flexible canopies and the induced coherent flow structures remain, however, 
    not partially understood.
    A large fraction of velocity measurements above and within flexible 
    canopies have relied on single-point measurements, with somewhat limited 
    studies capturing the spatial distribution and dynamics of the flow field. 
    \citet{okamoto2009turbulence, okamoto2013spatial} provided an understanding 
    of coherent flow structures and canopy motions using particle image velocimetry (PIV) 
    combined with simultaneous particle tracking velocimetry (PTV). In particular, 
    \citet{okamoto2009turbulence} suggested that coherent vortices are responsible for 
    the generation of monami, which in turn modulates momentum transfer. Recent investigation 
    \citep{okamoto2016flow} noted the initiation of monami by positive streamwise velocity 
    perturbations associated with vortices passing the canopy top, along with a strong correlation 
    between streamwise velocity fluctuations and canopy motion at a comparatively low frequency.
    Very recently, \citet{o2019dynamic} employed 2D numerical simulations to illustrate 
    that coupled interactions between the flow and canopy plate properties may be responsible 
    for coherent monami. Their parameterizations covered a range of mass ratios and bending 
    rigidities and enabled canopy and plate motion to be separated into four motion-based conditions, 
    namely, static, regular waving, irregular waving, and flapping. This variability in plate dynamics 
    was dependent on the relationship between natural blade frequency, and the mixing layer instability 
    frequency, in addition to sheltering effects caused by surrounding plates. The similarity of mixing 
    layer instability and blade natural frequency resulted in regular waving, whereas deviation from 
    this resulted in temporal and spatial differences in motion (irregular waving), or a uniform defected 
    state (static). The flapping state was characterized by the second mode natural frequency of the 
    plates, resulting in smaller flow structures than waving canopies, clearly indicating the role of 
    structural properties on motion dynamics.
    Besides, quantification of the distinct fluid dynamics from unsteady blades with reduced 
    motions within fully submerged, flexible canopies remains obscure. Necessary to advancing 
    such knowledge is the assessment of the plate motions and flow properties at high temporal and 
    spatial resolutions to uncover the distinct role of coherent motions. Here, we use a combination 
    of PIV and PTV to quantify the turbulence and plate motions in a canopy under very low Cauchy 
    numbers to assess the modulation of a fraction of plate motions in canopy turbulence; comparison 
    with a rigid case will help to evaluate such modulation further.  
    The experimental setup is described in $\S$2, measurements and discussion are 
    presented in $\S$3, and the main conclusions a summarized in $\S$4.
    \begin{figure}
        \centerline{\includegraphics[width=0.8\textwidth]{fig1}}
        \caption{Basic schematics of the flexible (and rigid) canopy. (\textit{a}) Top and $(b)$ side views of the staggered layout. The blue, dashed line indicates the location of the streamwise wall-normal PIV plane at the center of the canopy. Tip motions of the gray structures around the center were characterized with the PTV system.  (\textit{c}) Set-up illustrating the general dimensions, the two streamwise wall-normal FOVs covering the flexible canopy.}
        \label{canopy_model}
    \end{figure}
    \section{Experimental Setup}\label{sec:rules_submission}
    A canopy with a reduced flexibility and a rigid counterpart were placed fully submerged in a 2.5 m long,
    recirculating refractive-index-matching (RIM) flume of cross section 112.5 mm $\times$ 112.5 mm.  
    An aqueous sodium iodide solution of density $\rho_f = 1800$ kg m$^{-3}$ and kinematic 
    viscosity $\nu = 1.1 \times 10^{-6}$ m$^2$ s$^{-1}$ was used as working fluid. This technique 
    allowed measurements close to the wall, ensured uniform illumination in the interrogation regions 
    and optical access within the rigid canopy. Additional  information about RIM can be found 
    in \citet{blois2012versatile, bai2014refractive} and \citet{hamed2017impact}.
    The flexible and rigid canopies shared the same geometry characterized by prismatic blades of 
    height  $h=37.5$ mm, width $w=6.4$ mm or $h/w\approx 5.9$, and thickness $e=2$ mm. The blades were 
    distributed in a staggered pattern with streamwise and transverse spacing 
    of $S_x=\Delta x/w=1.56$ and $S_y= \Delta y/w=3.125$; see basic schematic in figure \ref{canopy_model}. 
    This resulted in a dense canopy with total frontal area per bed unit area of $\lambda_f = $ 
    1.2 \citep{finnigan2000turbulence}, and a frontal area per canopy volume of $a = n_sd =$ 32 m$^{-1}$. 
    It is worth pointing out that this arrangement is similar to that studied by \citet{hamed2017impact} 
    with rigid, heterogeneous canopies. The model canopies covered the transverse span of the flume, had 
    a streamwise length of $\Delta x/h\approx 5$ and was placed at $\Delta x/h\approx 19$ from the inlet. 
    There, the incoming boundary layer of $\delta=7.5$ mm induced  negligible effects on the canopy, which 
    was placed over a 5-mm acrylic base. The flexible canopy was casted from Silicone with a Young's Modulus 
    of $E$ = 2.05 MPa and density $\rho_m$ = 1030 kg m$^{-3}$.

    The motions of the blades within two columns along the streamwise span of the flexible canopy 
    and induced turbulence were explored under three bulk flows ($U_b$); whereas the turbulence induced 
    by the rigid canopy was inspected under one of the flow coinciding with the flexible counterpart. 
    Details of the corresponding Reynolds numbers $Re_H = U_{\infty}H/\nu$, the Froude 
    numbers $Fr = U_{\infty}/\sqrt{gH}$, Cauchy numbers $Ca = \rho_f b {U_0}^2 h^3/(EI)$ 
    \citep{luhar2016wave} and friction velocities at the canopy 
    height $u_* = -\langle u^\prime v^\prime\rangle ^{1/2}$ 
    \citep{poggi2004effect, nezu2008turburence, chen2013flow} are given in 
    table \ref{input}. Here, $g$ is the acceleration of gravity, $\langle \cdot \rangle$ is 
    the time-averaging operator, and primes denote fluctuating quantities.
    \begin{table}
        \begin{center}
            \def~{\hphantom{0}}
            \begin{tabular}{ccccccc}
    Case & Canopy & $U_{\infty}$  & $Re_H$   &   $Fr$ & $Ca$ & $u_*$ \\[3pt]
            &  & (m s$^{-1}$)   & ($\times 10^4$) & (-) & (-) & (m s$^{-1}$) \\
                F1 & Flexible & 0.18   & 1.84 & 0.17 & 2.3 & 0.019 \\
                F2 & Flexible & 0.27   & 2.76 & 0.26 & 5.1 & 0.028 \\
                F3 & Flexible & 0.36  & 3.68 & 0.34 & 9.0 & 0.040 \\
                R ($\Leftrightarrow$F2) & Rigid   & 0.27   & 2.76 & 0.26 & 5.1 & 0.028 \\
            \end{tabular}
            \caption{Experimental cases and basic parameters. The incoming flow on the rigid canopy R1 corresponded to the flexible canopy case in F2. }
            \label{input}
        \end{center}
    \end{table}
    Flow statistics and structure of the turbulence for each scenario were obtained with complementary 
    high-resolution and high-speed particle image velocimetry (PIV) systems from TSI.  Two fields of 
    view (FOV) located in the middle of the canopy models were illuminated by a 1 mm thick laser sheet 
    generated by a 250 mJ pulse$^{-1}$ double-pulsed laser from Quantel. Silver-coated, hollow glass 
    spheres of diameter 14 $\mu$m and density of 1700 kg m$^{-1}$ were used as seeding. Two thousand 
    image pairs were acquired by an 11 megapixel (4000 $\times$ 2672 pixels), 12-bit, frame straddle, 
    CCD camera. The image pairs were processed by the recursive cross-correlation method by using the 
    Insight 4G software from TSI. The final interrogation window was 24 $\times$ 24 pixels with 50$\%$ 
    overlap, resulting in a vector grid spacing $\Delta x = \Delta y = 720 \mu$m.
    The plates within the two central columns of the canopy were simultaneously tracked at a 
    frequency of 150 Hz during periods of 60 s, i.e., 9000 images, for every case. A Mikrotron 
    EoSens 4CXP MC 4082 camera at 2 MP resolution with a Nikon AF Micro-Nikkor 50 mm lens was 
    used for the tracking. The illumination was provided by two Stanley Lithium-Ion Halogen Spotlights. 
    The tips of each blade were carefully marked at the center to improve the motion tracking. Finally, 
    the raw images were processed with a pixel to distance ratio of 0.08 mm pixel$^{-1}$ by the open-source 
    OpenPTV. Detailed information on the PTV system can be found in \citet{kim2016three}. 
    Figure \ref{schematics} illustrates the basic characteristics of the setup.
'''
# %%
rx = re.compile(r'''(?<!\\)%.+|(\\(?:no)?cite.?\{((?!\*)[^{}]+)\})''')
authors = [m.group(2) for m in rx.finditer(latex) if m.group(2)]
# %%
authorList = []
for author in authors:
    newlist = author.split(', ')
    for ele in newlist:
        authorList.append(ele)
# %%
import bibtexparser
import pandas as pd
with open('reference.bib') as bibtex_file:
    bib_data = bibtexparser.load(bibtex_file)
entries = bib_data.entries

new_entries = []
for entry in entries:
    if entry['ID'] in authorList:
        new_entries.append(entry)
# %%
db = bibtexparser.bibdatabase.BibDatabase()
db.entries = new_entries
writer = bibtexparser.bwriter.BibTexWriter()
with open('newbibtex.bib', 'w') as bibfile:
    bibfile.write(writer.write(db))
# %%
import sys
for entry in new_entries:
    with open('newbibtem.txt', 'a') as oitems:
        
        authorList = entry['author']
        authorList = authorList.split(' and ')
        
        NumAuthor = len(authorList)
        
        NewAuthorList = []
        for authorName in authorList:
            authorNameList = authorName.split(', ')
            newAuthorName = authorNameList[0]
            if len(authorNameList) > 1:
                rest = [char for char in authorNameList[1] if char.isupper()]
                for letter in rest:
                    newAuthorName = newAuthorName + ', ' + letter + '.'
                NewAuthorList.append(newAuthorName)

        referenceAuthor = ''
        for i in range(len(NewAuthorList)):
            if i == 0:
                referenceAuthor = referenceAuthor + NewAuthorList[i]
            elif i == NumAuthor - 1:
                referenceAuthor = referenceAuthor + ' {\&} ' + NewAuthorList[i]
            else:
                referenceAuthor = referenceAuthor + ', ' + NewAuthorList[i]
            
        
        if NumAuthor >= 3:
            first = NewAuthorList[0].split(',')
            first = first[0]
            label = first + ' et al.' + '({})'.format(entry['year'])
        else:
            label = referenceAuthor +  '({})'.format(entry['year'])   
        
        
        oitems.write('\\bibitem' + '[{}]'.format(label) + '{%s}' % entry['ID'])
        oitems.write('\n')
        if entry['author']:
            oitems.write(referenceAuthor + '({})'.format(entry['year']))
            #oitems.write(entry['author'] + '({})'.format(entry['year']))
        oitems.write('\n') 
        if entry['title']:
            oitems.write('{}.'.format(entry['title']))
        oitems.write('\n')
        if 'journal' in entry.keys():
            oitems.write(r' \textit{' + entry['journal'] + '}') 
        elif 'booktitle' in entry.keys():
            oitems.write(r' \textit{' + entry['booktitle'] + '}')   
        elif 'publisher' in entry.keys():
            oitems.write(r' \textit{' + entry['publisher'] + '}') 
        else:
            print('Error: no journal, book, or publisher')
            break
        if 'volume' in entry.keys():
            oitems.write(r', \textit{'+entry['volume']+'}')
            if 'number' in entry.keys():
                oitems.write('({})'.format(entry['number']))
        if 'pages' in entry.keys():
            oitems.write(', {}'.format(entry['pages']))
        oitems.write('.')
            
        oitems.write('\n') 
        oitems.write('\n')   
            
            
# %%
