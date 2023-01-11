
        from pymol import cmd,stored
        
        set depth_cue, 1
        set fog_start, 0.4
        
        set_color b_col, [36,36,85]
        set_color t_col, [10,10,10]
        set bg_rgb_bottom, b_col
        set bg_rgb_top, t_col      
        set bg_gradient
        
        set  spec_power  =  200
        set  spec_refl   =  0
        
        load "data/6zsl_chainA.pdb", protein
        create ligands, protein and organic
        select xlig, protein and organic
        delete xlig
        
        hide everything, all
        
        color white, elem c
        color bluewhite, protein
        #show_as cartoon, protein
        show surface, protein
        #set transparency, 0.15
        
        show sticks, ligands
        set stick_color, magenta
        
        
        
        
        # SAS points
 
        load "data/6zsl_chainA.pdb_points.pdb.gz", points
        hide nonbonded, points
        show nb_spheres, points
        set sphere_scale, 0.2, points
        cmd.spectrum("b", "green_red", selection="points", minimum=0, maximum=0.7)
        
        
        stored.list=[]
        cmd.iterate("(resn STP)","stored.list.append(resi)")    # read info about residues STP
        lastSTP=stored.list[-1] # get the index of the last residue
        hide lines, resn STP
        
        cmd.select("rest", "resn STP and resi 0")
        
        for my_index in range(1,int(lastSTP)+1): cmd.select("pocket"+str(my_index), "resn STP and resi "+str(my_index))
        for my_index in range(1,int(lastSTP)+1): cmd.show("spheres","pocket"+str(my_index))
        for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_scale","0.4","pocket"+str(my_index))
        for my_index in range(1,int(lastSTP)+1): cmd.set("sphere_transparency","0.1","pocket"+str(my_index))
        
        
        
        set_color pcol1 = [0.361,0.576,0.902]
select surf_pocket1, protein and id [7232,8486,6540,6541,7214,7215,7216,7208,7211,7416,7209,6529,6530,6552,6553,6547,6780,6782,6542,6546,6548,6554,6512,7445,7446,7447,6518,6519,6520,6521,7739,8502,8503,7748,7751,7752,8504,8505,6750,6749,8481,8487,8488,8489,8490,8725,6726,6730,6727,6723,6724,6725,7217,7218] 
set surface_color,  pcol1, surf_pocket1 
set_color pcol2 = [0.329,0.278,0.702]
select surf_pocket2, protein and id [5774,5786,5797,5798,5799,8337,8314,8325,8327,8087,8088,8330,7469,7472,8616,8620,8621,7473,8464,8465,8623,8668,8624,8462,8463,8448,8449,8083,5768] 
set surface_color,  pcol2, surf_pocket2 
set_color pcol3 = [0.698,0.361,0.902]
select surf_pocket3, protein and id [7539,8642,7591,8643,8644,8657,8658,8659,7558,7559,7540,7528,7530,7536,7466,7480,7543,7461,7462,7508,7469,8616,8621,8668,7475,7535,8613,8615,8641] 
set surface_color,  pcol3, surf_pocket3 
set_color pcol4 = [0.702,0.278,0.639]
select surf_pocket4, protein and id [5358,5419,7257,7260,7253,5450,5453,7261,7250,7251,7265,7482,7483,7584,5367,7572,5477,5359,5446,5447,5449,5334] 
set surface_color,  pcol4, surf_pocket4 
set_color pcol5 = [0.902,0.361,0.545]
select surf_pocket5, protein and id [4542,4526,4529,4678,4680,4523,5400,5402,5403,4541,5427,5433,5434,5461,5439,5462,4645,4656,4665,4668,5429,6136] 
set surface_color,  pcol5, surf_pocket5 
set_color pcol6 = [0.702,0.353,0.278]
select surf_pocket6, protein and id [5176,5183,5167,5169,5171,5173,4844,4845,4830,4861,4863,5000,5016,5018,4987,4593,4837,5181,5182] 
set surface_color,  pcol6, surf_pocket6 
set_color pcol7 = [0.902,0.729,0.361]
select surf_pocket7, protein and id [7471,7112,5502,5514,5516,5515,5541,5543,5503,7491,7492,5506,5507,7251,7252,5485,5486,7280,7279,7467,5505] 
set surface_color,  pcol7, surf_pocket7 
   
        
        deselect
        
        orient
        