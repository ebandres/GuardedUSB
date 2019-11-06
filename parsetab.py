
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftTkAsigleftTkAndTkOrnonassocTkLessTkLeqTkGeqTkGreaterleftTkPlusTkMinusleftTkMultTkDivTkModleftTkEqualTkNEqualrightTkNotleftTkOBracketTkCBracketleftTkConcatrightTkArrowTkAnd TkArray TkArrow TkAsig TkAtoi TkBool TkCBlock TkCBracket TkClosePar TkComma TkConcat TkDeclare TkDiv TkDo TkEqual TkFalse TkFi TkFor TkGeq TkGreater TkGuard TkId TkIf TkIn TkInt TkLeq TkLess TkMax TkMin TkMinus TkMod TkMult TkNEqual TkNot TkNum TkOBlock TkOBracket TkOd TkOpenPar TkOr TkPlus TkPrint TkPrintln TkRead TkRof TkSemiColon TkSize TkSoForth TkString TkTo TkTrue TkTwoPointsblock : TkOBlock TkDeclare start TkCBlock\n             | TkOBlock body TkCBlockbody : sentence body\n            | sentcond body\n            | unique\n            | terminal start : declaration start\n              | declaration bodyempty :declaration : TkId TkTwoPoints tipo TkSemiColon\n                   | TkId TkComma listaid TkTwoPoints tipo TkSemiColonlistaid : TkId TkComma listaid\n               | TkIdtipo : TkInt\n            | TkBool\n            | TkArray TkOBracket TkNum TkSoForth TkNum TkCBracketassign : TkId TkAsig expressionassign : TkId TkAsig strexpassign : TkId TkAsig arrayarray : TkNum TkComma array\n             | TkNumstrexp : TkString TkConcat strexp\n              | TkStringexpression : expression TkPlus expression\n                  | expression TkMinus expression\n                  | expression TkMult expression\n                  | expression TkDiv expression\n                  | expression TkMod expressionexpression : TkOpenPar expression TkCloseParexpression : TkSize TkOpenPar TkId TkClosePar\n                  | TkMax TkOpenPar TkId TkClosePar\n                  | TkMin TkOpenPar TkId TkClosePar\n                  | TkAtoi TkOpenPar TkId TkCloseParexpression : TkNum\n                  | TkId TkOBracket expression TkCBracketexpression : TkIdexpression : expression TkLess expression\n                  | expression TkLeq expression\n                  | expression TkGeq expression\n                  | expression TkGreater expression\n                  | expression TkOr expression\n                  | expression TkAnd expression\n                  | expression TkEqual expression\n                  | expression TkNEqual expressionexpression : TkTrueexpression : TkFalseexpression : TkNot expressionread : TkRead TkIdgfor : TkFor TkId TkIn expression TkTo expression TkArrow block TkRofgdo : TkDo expression TkArrow unique guard TkOd\n\t\t   | TkDo expression TkArrow block guard TkOdgif : TkIf expression TkArrow unique guard TkFi  \n           | TkIf expression TkArrow block guard TkFi sentence : assign TkSemiColon\n                | gprint TkSemiColon\n                | gprintln TkSemiColon\n                | read TkSemiColonsentcond : gif TkSemiColon\n                | gdo TkSemiColon\n                | gfor TkSemiColonterminal : gif\n                | gdo\n                | gforunique : assign\n              | gprint\n              | gprintlnguard : TkGuard expression TkArrow unique guard\n             | TkGuard expression TkArrow block guard\n             | emptygprint : TkPrint strprintgprintln : TkPrintln strprintstrprint : strprint TkConcat strprint\n                | TkString\n                | expression'
    
_lr_action_items = {'TkOBlock':([0,87,88,156,157,],[2,2,2,2,2,]),'$end':([1,26,55,],[0,-2,-1,]),'TkDeclare':([2,],[3,]),'TkId':([2,3,5,6,17,18,19,20,21,22,24,29,30,31,32,33,34,35,36,40,49,60,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,87,88,89,126,128,139,144,155,156,],[16,25,16,16,42,42,51,42,42,54,58,-54,-55,-56,-57,-58,-59,-60,42,42,42,94,42,42,42,42,42,42,42,42,42,42,42,42,42,42,113,42,115,116,117,16,16,42,-10,94,42,42,-11,16,]),'TkPrint':([2,5,6,24,29,30,31,32,33,34,35,87,88,126,155,156,],[17,17,17,17,-54,-55,-56,-57,-58,-59,-60,17,17,-10,-11,17,]),'TkPrintln':([2,5,6,24,29,30,31,32,33,34,35,87,88,126,155,156,],[18,18,18,18,-54,-55,-56,-57,-58,-59,-60,18,18,-10,-11,18,]),'TkRead':([2,5,6,24,29,30,31,32,33,34,35,126,155,],[19,19,19,19,-54,-55,-56,-57,-58,-59,-60,-10,-11,]),'TkIf':([2,5,6,24,29,30,31,32,33,34,35,126,155,],[20,20,20,20,-54,-55,-56,-57,-58,-59,-60,-10,-11,]),'TkDo':([2,5,6,24,29,30,31,32,33,34,35,126,155,],[21,21,21,21,-54,-55,-56,-57,-58,-59,-60,-10,-11,]),'TkFor':([2,5,6,24,29,30,31,32,33,34,35,126,155,],[22,22,22,22,-54,-55,-56,-57,-58,-59,-60,-10,-11,]),'TkCBlock':([4,7,8,9,10,11,13,14,15,23,27,28,37,38,39,42,46,47,48,50,56,57,61,62,63,64,65,86,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,130,131,132,133,134,135,136,137,148,150,151,152,165,],[26,-5,-6,-64,-65,-66,-61,-62,-63,55,-3,-4,-70,-73,-74,-36,-34,-45,-46,-71,-7,-8,-17,-18,-19,-21,-23,-47,-72,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,-21,-20,-22,-30,-35,-31,-32,-33,-52,-53,-50,-51,-49,]),'TkSemiColon':([9,10,11,12,13,14,15,37,38,39,42,46,47,48,50,51,61,62,63,64,65,86,90,91,92,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,130,131,132,133,134,135,136,137,147,148,150,151,152,162,165,],[29,30,31,32,33,34,35,-70,-73,-74,-36,-34,-45,-46,-71,-48,-17,-18,-19,-21,-23,-47,126,-14,-15,-72,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,-21,-20,-22,-30,-35,-31,-32,-33,155,-52,-53,-50,-51,-16,-49,]),'TkAsig':([16,58,],[36,36,]),'TkString':([17,18,36,66,97,],[38,38,65,38,65,]),'TkOpenPar':([17,18,20,21,36,40,41,43,44,45,49,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,89,139,144,],[40,40,40,40,40,40,81,83,84,85,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'TkSize':([17,18,20,21,36,40,49,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,89,139,144,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'TkMax':([17,18,20,21,36,40,49,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,89,139,144,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'TkMin':([17,18,20,21,36,40,49,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,89,139,144,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'TkAtoi':([17,18,20,21,36,40,49,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,89,139,144,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'TkNum':([17,18,20,21,36,40,49,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,89,96,127,139,144,154,],[46,46,46,46,64,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,130,145,46,46,158,]),'TkTrue':([17,18,20,21,36,40,49,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,89,139,144,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'TkFalse':([17,18,20,21,36,40,49,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,89,139,144,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'TkNot':([17,18,20,21,36,40,49,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,89,139,144,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'TkTwoPoints':([25,58,94,95,146,],[59,59,-13,129,-12,]),'TkComma':([25,58,64,94,130,],[60,60,96,128,96,]),'TkGuard':([26,37,38,39,42,46,47,48,50,55,61,62,63,64,65,86,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,118,119,120,121,122,123,124,130,131,132,133,134,135,136,137,159,160,],[-2,-70,-73,-74,-36,-34,-45,-46,-71,-1,-17,-18,-19,-21,-23,-47,-72,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,139,139,-64,-65,-66,139,139,-21,-20,-22,-30,-35,-31,-32,-33,139,139,]),'TkFi':([26,37,38,39,42,46,47,48,50,55,61,62,63,64,65,86,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,118,119,120,121,122,130,131,132,133,134,135,136,137,138,140,141,159,160,163,164,],[-2,-70,-73,-74,-36,-34,-45,-46,-71,-1,-17,-18,-19,-21,-23,-47,-72,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,-9,-9,-64,-65,-66,-21,-20,-22,-30,-35,-31,-32,-33,148,-69,150,-9,-9,-67,-68,]),'TkOd':([26,37,38,39,42,46,47,48,50,55,61,62,63,64,65,86,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,120,121,122,123,124,130,131,132,133,134,135,136,137,140,142,143,159,160,163,164,],[-2,-70,-73,-74,-36,-34,-45,-46,-71,-1,-17,-18,-19,-21,-23,-47,-72,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,-64,-65,-66,-9,-9,-21,-20,-22,-30,-35,-31,-32,-33,-69,151,152,-9,-9,-67,-68,]),'TkRof':([26,55,161,],[-2,-1,165,]),'TkConcat':([37,38,39,42,46,47,48,50,65,86,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,133,134,135,136,137,],[66,-73,-74,-36,-34,-45,-46,66,97,-47,-72,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,-30,-35,-31,-32,-33,]),'TkPlus':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[67,-36,-34,-45,-46,67,67,67,-34,67,-47,-24,-25,-26,-27,-28,67,67,67,67,67,67,-43,-44,-29,67,67,-30,-35,-31,-32,-33,67,67,]),'TkMinus':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[68,-36,-34,-45,-46,68,68,68,-34,68,-47,-24,-25,-26,-27,-28,68,68,68,68,68,68,-43,-44,-29,68,68,-30,-35,-31,-32,-33,68,68,]),'TkMult':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[69,-36,-34,-45,-46,69,69,69,-34,69,-47,69,69,-26,-27,-28,69,69,69,69,69,69,-43,-44,-29,69,69,-30,-35,-31,-32,-33,69,69,]),'TkDiv':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[70,-36,-34,-45,-46,70,70,70,-34,70,-47,70,70,-26,-27,-28,70,70,70,70,70,70,-43,-44,-29,70,70,-30,-35,-31,-32,-33,70,70,]),'TkMod':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[71,-36,-34,-45,-46,71,71,71,-34,71,-47,71,71,-26,-27,-28,71,71,71,71,71,71,-43,-44,-29,71,71,-30,-35,-31,-32,-33,71,71,]),'TkLess':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[72,-36,-34,-45,-46,72,72,72,-34,72,-47,-24,-25,-26,-27,-28,None,None,None,None,72,72,-43,-44,-29,72,72,-30,-35,-31,-32,-33,72,72,]),'TkLeq':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[73,-36,-34,-45,-46,73,73,73,-34,73,-47,-24,-25,-26,-27,-28,None,None,None,None,73,73,-43,-44,-29,73,73,-30,-35,-31,-32,-33,73,73,]),'TkGeq':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[74,-36,-34,-45,-46,74,74,74,-34,74,-47,-24,-25,-26,-27,-28,None,None,None,None,74,74,-43,-44,-29,74,74,-30,-35,-31,-32,-33,74,74,]),'TkGreater':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[75,-36,-34,-45,-46,75,75,75,-34,75,-47,-24,-25,-26,-27,-28,None,None,None,None,75,75,-43,-44,-29,75,75,-30,-35,-31,-32,-33,75,75,]),'TkOr':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[76,-36,-34,-45,-46,76,76,76,-34,76,-47,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,76,76,-30,-35,-31,-32,-33,76,76,]),'TkAnd':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[77,-36,-34,-45,-46,77,77,77,-34,77,-47,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,77,77,-30,-35,-31,-32,-33,77,77,]),'TkEqual':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[78,-36,-34,-45,-46,78,78,78,-34,78,-47,78,78,78,78,78,78,78,78,78,78,78,-43,-44,-29,78,78,-30,-35,-31,-32,-33,78,78,]),'TkNEqual':([39,42,46,47,48,52,53,61,64,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,125,133,134,135,136,137,149,153,],[79,-36,-34,-45,-46,79,79,79,-34,79,-47,79,79,79,79,79,79,79,79,79,79,79,-43,-44,-29,79,79,-30,-35,-31,-32,-33,79,79,]),'TkOBracket':([42,93,],[82,127,]),'TkArrow':([42,46,47,48,52,53,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,133,134,135,136,137,149,153,],[-36,-34,-45,-46,87,88,-47,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,-30,-35,-31,-32,-33,156,157,]),'TkClosePar':([42,46,47,48,80,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,117,133,134,135,136,137,],[-36,-34,-45,-46,112,-47,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,133,135,136,137,-30,-35,-31,-32,-33,]),'TkCBracket':([42,46,47,48,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,133,134,135,136,137,158,],[-36,-34,-45,-46,-47,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,134,-30,-35,-31,-32,-33,162,]),'TkTo':([42,46,47,48,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,125,133,134,135,136,137,],[-36,-34,-45,-46,-47,-24,-25,-26,-27,-28,-37,-38,-39,-40,-41,-42,-43,-44,-29,144,-30,-35,-31,-32,-33,]),'TkIn':([54,],[89,]),'TkInt':([59,129,],[91,91,]),'TkBool':([59,129,],[92,92,]),'TkArray':([59,129,],[93,93,]),'TkSoForth':([145,],[154,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'block':([0,87,88,156,157,],[1,119,124,160,161,]),'body':([2,5,6,24,],[4,27,28,57,]),'sentence':([2,5,6,24,],[5,5,5,5,]),'sentcond':([2,5,6,24,],[6,6,6,6,]),'unique':([2,5,6,24,87,88,156,],[7,7,7,7,118,123,159,]),'terminal':([2,5,6,24,],[8,8,8,8,]),'assign':([2,5,6,24,87,88,156,],[9,9,9,9,120,120,120,]),'gprint':([2,5,6,24,87,88,156,],[10,10,10,10,121,121,121,]),'gprintln':([2,5,6,24,87,88,156,],[11,11,11,11,122,122,122,]),'read':([2,5,6,24,],[12,12,12,12,]),'gif':([2,5,6,24,],[13,13,13,13,]),'gdo':([2,5,6,24,],[14,14,14,14,]),'gfor':([2,5,6,24,],[15,15,15,15,]),'start':([3,24,],[23,56,]),'declaration':([3,24,],[24,24,]),'strprint':([17,18,66,],[37,50,98,]),'expression':([17,18,20,21,36,40,49,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,89,139,144,],[39,39,52,53,61,80,86,39,99,100,101,102,103,104,105,106,107,108,109,110,111,114,125,149,153,]),'strexp':([36,97,],[62,132,]),'array':([36,96,],[63,131,]),'tipo':([59,129,],[90,147,]),'listaid':([60,128,],[95,146,]),'guard':([118,119,123,124,159,160,],[138,141,142,143,163,164,]),'empty':([118,119,123,124,159,160,],[140,140,140,140,140,140,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> block","S'",1,None,None,None),
  ('block -> TkOBlock TkDeclare start TkCBlock','block',4,'p_code','Parser.py',31),
  ('block -> TkOBlock body TkCBlock','block',3,'p_code','Parser.py',32),
  ('body -> sentence body','body',2,'p_body','Parser.py',42),
  ('body -> sentcond body','body',2,'p_body','Parser.py',43),
  ('body -> unique','body',1,'p_body','Parser.py',44),
  ('body -> terminal','body',1,'p_body','Parser.py',45),
  ('start -> declaration start','start',2,'p_start','Parser.py',55),
  ('start -> declaration body','start',2,'p_start','Parser.py',56),
  ('empty -> <empty>','empty',0,'p_empty','Parser.py',60),
  ('declaration -> TkId TkTwoPoints tipo TkSemiColon','declaration',4,'p_declaration','Parser.py',64),
  ('declaration -> TkId TkComma listaid TkTwoPoints tipo TkSemiColon','declaration',6,'p_declaration','Parser.py',65),
  ('listaid -> TkId TkComma listaid','listaid',3,'p_listid','Parser.py',72),
  ('listaid -> TkId','listaid',1,'p_listid','Parser.py',73),
  ('tipo -> TkInt','tipo',1,'p_tipo','Parser.py',80),
  ('tipo -> TkBool','tipo',1,'p_tipo','Parser.py',81),
  ('tipo -> TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket','tipo',6,'p_tipo','Parser.py',82),
  ('assign -> TkId TkAsig expression','assign',3,'p_assign_expr','Parser.py',85),
  ('assign -> TkId TkAsig strexp','assign',3,'p_assign_str','Parser.py',96),
  ('assign -> TkId TkAsig array','assign',3,'p_assign_arr','Parser.py',106),
  ('array -> TkNum TkComma array','array',3,'p_array','Parser.py',116),
  ('array -> TkNum','array',1,'p_array','Parser.py',117),
  ('strexp -> TkString TkConcat strexp','strexp',3,'p_expression_str','Parser.py',120),
  ('strexp -> TkString','strexp',1,'p_expression_str','Parser.py',121),
  ('expression -> expression TkPlus expression','expression',3,'p_expression_bin','Parser.py',125),
  ('expression -> expression TkMinus expression','expression',3,'p_expression_bin','Parser.py',126),
  ('expression -> expression TkMult expression','expression',3,'p_expression_bin','Parser.py',127),
  ('expression -> expression TkDiv expression','expression',3,'p_expression_bin','Parser.py',128),
  ('expression -> expression TkMod expression','expression',3,'p_expression_bin','Parser.py',129),
  ('expression -> TkOpenPar expression TkClosePar','expression',3,'p_expression_group','Parser.py',151),
  ('expression -> TkSize TkOpenPar TkId TkClosePar','expression',4,'p_expression_fun','Parser.py',156),
  ('expression -> TkMax TkOpenPar TkId TkClosePar','expression',4,'p_expression_fun','Parser.py',157),
  ('expression -> TkMin TkOpenPar TkId TkClosePar','expression',4,'p_expression_fun','Parser.py',158),
  ('expression -> TkAtoi TkOpenPar TkId TkClosePar','expression',4,'p_expression_fun','Parser.py',159),
  ('expression -> TkNum','expression',1,'p_expression_number','Parser.py',169),
  ('expression -> TkId TkOBracket expression TkCBracket','expression',4,'p_expression_number','Parser.py',170),
  ('expression -> TkId','expression',1,'p_expression_id','Parser.py',176),
  ('expression -> expression TkLess expression','expression',3,'p_boolean_exp','Parser.py',185),
  ('expression -> expression TkLeq expression','expression',3,'p_boolean_exp','Parser.py',186),
  ('expression -> expression TkGeq expression','expression',3,'p_boolean_exp','Parser.py',187),
  ('expression -> expression TkGreater expression','expression',3,'p_boolean_exp','Parser.py',188),
  ('expression -> expression TkOr expression','expression',3,'p_boolean_exp','Parser.py',189),
  ('expression -> expression TkAnd expression','expression',3,'p_boolean_exp','Parser.py',190),
  ('expression -> expression TkEqual expression','expression',3,'p_boolean_exp','Parser.py',191),
  ('expression -> expression TkNEqual expression','expression',3,'p_boolean_exp','Parser.py',192),
  ('expression -> TkTrue','expression',1,'p_expression_true','Parser.py',226),
  ('expression -> TkFalse','expression',1,'p_expression_false','Parser.py',232),
  ('expression -> TkNot expression','expression',2,'p_expression_not','Parser.py',239),
  ('read -> TkRead TkId','read',2,'p_read','Parser.py',243),
  ('gfor -> TkFor TkId TkIn expression TkTo expression TkArrow block TkRof','gfor',9,'p_cycle_for','Parser.py',254),
  ('gdo -> TkDo expression TkArrow unique guard TkOd','gdo',6,'p_cycle_do','Parser.py',263),
  ('gdo -> TkDo expression TkArrow block guard TkOd','gdo',6,'p_cycle_do','Parser.py',264),
  ('gif -> TkIf expression TkArrow unique guard TkFi','gif',6,'p_if','Parser.py',268),
  ('gif -> TkIf expression TkArrow block guard TkFi','gif',6,'p_if','Parser.py',269),
  ('sentence -> assign TkSemiColon','sentence',2,'p_sentence','Parser.py',273),
  ('sentence -> gprint TkSemiColon','sentence',2,'p_sentence','Parser.py',274),
  ('sentence -> gprintln TkSemiColon','sentence',2,'p_sentence','Parser.py',275),
  ('sentence -> read TkSemiColon','sentence',2,'p_sentence','Parser.py',276),
  ('sentcond -> gif TkSemiColon','sentcond',2,'p_sentence_cond','Parser.py',281),
  ('sentcond -> gdo TkSemiColon','sentcond',2,'p_sentence_cond','Parser.py',282),
  ('sentcond -> gfor TkSemiColon','sentcond',2,'p_sentence_cond','Parser.py',283),
  ('terminal -> gif','terminal',1,'p_terminal','Parser.py',287),
  ('terminal -> gdo','terminal',1,'p_terminal','Parser.py',288),
  ('terminal -> gfor','terminal',1,'p_terminal','Parser.py',289),
  ('unique -> assign','unique',1,'p_unique','Parser.py',293),
  ('unique -> gprint','unique',1,'p_unique','Parser.py',294),
  ('unique -> gprintln','unique',1,'p_unique','Parser.py',295),
  ('guard -> TkGuard expression TkArrow unique guard','guard',5,'p_guard','Parser.py',299),
  ('guard -> TkGuard expression TkArrow block guard','guard',5,'p_guard','Parser.py',300),
  ('guard -> empty','guard',1,'p_guard','Parser.py',301),
  ('gprint -> TkPrint strprint','gprint',2,'p_print','Parser.py',306),
  ('gprintln -> TkPrintln strprint','gprintln',2,'p_println','Parser.py',310),
  ('strprint -> strprint TkConcat strprint','strprint',3,'p_strprint','Parser.py',314),
  ('strprint -> TkString','strprint',1,'p_strprint','Parser.py',315),
  ('strprint -> expression','strprint',1,'p_strprint','Parser.py',316),
]
