# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 21:29:28 2025

@author: kshit
"""
def dcf_engine(grate, rev0, ebit0, da0, nwc0, capex0, yrs, taxrate, equityval, debtval, r_e, r_d, cash, debt, no_shares, foreverg):
    #defining % of revenue of each term necessary
    ebitrate = ebit0/rev0
    darate = da0/rev0
    nwcrate = nwc0/rev0
    capexrate = capex0/rev0
    #making a list of all revenue terms
    revlist = [rev0]
    #same with all ufcf terms
    ufcf_list = []
    #for number of years
    for i in range(yrs):
        #rev1 is the last term of the revenue list with added growth rate
        rev1 = revlist[-1]+revlist[-1]*grate
        #updating the revenue list to include the latest revenue at the end
        revlist.append(rev1)
        ebit1 = rev1*ebitrate
        #calculating ufcf
        ufcf1 = ebit1*(1-taxrate) + rev1*darate - rev1*nwcrate - capexrate*rev1
        #adding the latest ufcf calculated to the end of the list
        ufcf_list.append(ufcf1)
    #defining v to calculate wacc
    totalval = equityval+debtval
    #wacc to be used
    wacc = (equityval/totalval)*r_e + (debtval/totalval)*r_d*(1-taxrate)
    waccden = 1+wacc
    pv_ufcf_list = []
    y = 1 
    c = 0
    for i in ufcf_list:
        pv_ufcf = ufcf_list[c]/waccden**y
        pv_ufcf_list.append(pv_ufcf)
        y = y+1 
        c = c+1
        #calculate pv of each term in ufcf list sumn like = i/(1+wacc)^y..... then y = y+1
    #calculate present value of terminal value
    final_fcf = ufcf_list[-1]
    terminalval = final_fcf*(1+foreverg)/(wacc-foreverg)
    pv_terminalval = terminalval/waccden**yrs
    enterpriseval = sum(pv_ufcf_list) + pv_terminalval
    net_debt = debt - cash
    eqvalue = enterpriseval - net_debt
    sprice = eqvalue/no_shares
    print("The enterprise value is", enterpriseval, " The equity value is", eqvalue, "and the share price is", sprice)
