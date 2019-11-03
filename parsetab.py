
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftTkAsignonassocTkLessTkLeqTkGeqTkGreaterleftTkPlusTkMinusleftTkMultTkDivTkModleftTkEqualTkNEqualleftTkAndTkOrrightTkNotleftTkOBracketTkCBracketleftTkConcatrightTkArrowTkAnd TkArray TkArrow TkAsig TkAtoi TkCBlock TkCBracket TkClosePar TkComma TkConcat TkDeclare TkDiv TkDo TkEqual TkFalse TkFi TkFor TkGeq TkGreater TkGuard TkId TkIf TkIn TkInt TkLeq TkLess TkMax TkMin TkMinus TkMod TkMult TkNEqual TkNot TkNum TkOBlock TkOBracket TkOd TkOpenPar TkOr TkPlus TkPrint TkPrintln TkRead TkRof TkSemiColon TkSize TkSoForth TkString TkTo TkTrue TkTwoPointsblock : TkOBlock TkDeclare start TkCBlock\n             | TkOBlock body TkCBlockbody : sentence body\n            | gfor body\n            | read body\n            | gdo body\n            | gif body\n            | empty start : declaration start\n              | bodyempty :declaration : TkId TkTwoPoints tipo TkSemiColon\n                   | TkId TkComma listaid TkTwoPoints tipo TkSemiColonlistaid : TkId TkComma listaid\n               | TkIdtipo : TkInt\n            | TkArray TkOBracket TkNum TkSoForth TkNum TkCBracketassign : TkId TkAsig expressionassign : TkId TkAsig strexpassign : TkId TkAsig arrayarray : TkOBracket inarray TkCBracket\n             | TkOBracket TkNum TkSoForth TkNum TkCBracketinarray : TkNum TkComma inarray\n               | TkNumstrexp : TkString TkConcat strexp\n              | TkStringexpression : expression TkPlus expression\n                  | expression TkMinus expression\n                  | expression TkMult expression\n                  | expression TkDiv expression\n                  | expression TkMod expressionexpression : TkOpenPar expression TkCloseParexpression : TkSize TkOpenPar TkId TkClosePar\n                  | TkMax TkOpenPar TkId TkClosePar\n                  | TkMin TkOpenPar TkId TkClosePar\n                  | TkAtoi TkOpenPar TkId TkCloseParexpression : TkNumexpression : TkIdboolean : expression TkLess expression\n               | expression TkLeq expression\n               | expression TkGeq expression\n               | expression TkGreater expression\n               | boolean TkOr boolean\n               | boolean TkAnd boolean\n               | expression TkEqual expression\n               | expression TkEqual boolean\n               | boolean TkEqual expression\n               | boolean TkEqual boolean\n               | expression TkNEqual expression\n               | expression TkNEqual boolean\n               | boolean TkNEqual expression\n               | boolean TkNEqual booleanboolean : TkOpenPar boolean TkCloseParboolean : TkTrueboolean : TkFalseboolean : TkNot booleanread : TkRead TkId TkSemiColongfor : TkFor TkId TkIn expression TkTo expression TkArrow block TkRof TkSemiColongdo : TkDo boolean TkArrow block TkOd TkSemiColongif : TkIf boolean TkArrow unique guard TkFi TkSemiColon\n           | TkIf boolean TkArrow block guard TkFi TkSemiColonsentence : assign TkSemiColon\n                | gprint TkSemiColon\n                | gprintln TkSemiColonunique : assign\n              | gprint\n              | gprintlnguard : TkGuard boolean TkArrow unique guard\n             | TkGuard boolean TkArrow block guard\n             | emptygprint : TkPrint strprintgprintln : TkPrintln strprintstrprint : TkString TkConcat strprint\n                | TkId TkConcat strprint\n                | TkString\n                | TkId'
    
_lr_action_items = {'TkOBlock':([0,66,89,168,171,],[2,2,2,2,2,]),'$end':([1,25,54,],[0,-2,-1,]),'TkDeclare':([2,],[3,]),'TkFor':([2,3,5,6,7,8,9,22,31,32,33,65,136,162,167,170,172,181,],[14,14,14,14,14,14,14,14,-62,-63,-64,-57,-12,-59,-13,-60,-61,-58,]),'TkRead':([2,3,5,6,7,8,9,22,31,32,33,65,136,162,167,170,172,181,],[16,16,16,16,16,16,16,16,-62,-63,-64,-57,-12,-59,-13,-60,-61,-58,]),'TkDo':([2,3,5,6,7,8,9,22,31,32,33,65,136,162,167,170,172,181,],[17,17,17,17,17,17,17,17,-62,-63,-64,-57,-12,-59,-13,-60,-61,-58,]),'TkIf':([2,3,5,6,7,8,9,22,31,32,33,65,136,162,167,170,172,181,],[18,18,18,18,18,18,18,18,-62,-63,-64,-57,-12,-59,-13,-60,-61,-58,]),'TkCBlock':([2,3,4,5,6,7,8,9,10,21,22,23,26,27,28,29,30,31,32,33,55,65,136,162,167,170,172,181,],[-11,-11,25,-11,-11,-11,-11,-11,-8,54,-11,-10,-3,-4,-5,-6,-7,-62,-63,-64,-9,-57,-12,-59,-13,-60,-61,-58,]),'TkId':([2,3,5,6,7,8,9,14,16,17,18,19,20,22,31,32,33,35,39,42,57,58,62,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,88,89,90,91,107,136,138,140,152,162,167,170,171,172,181,],[15,24,15,15,15,15,15,34,36,44,44,52,52,24,-62,-63,-64,44,44,44,95,44,44,-57,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,125,126,127,128,15,52,52,44,-12,95,44,44,-59,-13,-60,15,-61,-58,]),'TkPrint':([2,3,5,6,7,8,9,22,31,32,33,65,89,136,162,167,170,171,172,181,],[19,19,19,19,19,19,19,19,-62,-63,-64,-57,19,-12,-59,-13,-60,19,-61,-58,]),'TkPrintln':([2,3,5,6,7,8,9,22,31,32,33,65,89,136,162,167,170,171,172,181,],[20,20,20,20,20,20,20,20,-62,-63,-64,-57,20,-12,-59,-13,-60,20,-61,-58,]),'TkSemiColon':([11,12,13,36,44,48,50,51,52,53,59,60,61,63,92,93,118,119,120,121,122,124,134,135,141,142,145,147,148,149,150,157,163,165,169,177,178,],[31,32,33,65,-38,-37,-71,-75,-76,-72,-18,-19,-20,-26,136,-16,-27,-28,-29,-30,-31,-32,-73,-74,-25,-21,162,-33,-34,-35,-36,167,170,172,-22,-17,181,]),'TkAsig':([15,24,],[35,35,]),'TkOpenPar':([17,18,35,39,42,43,45,46,47,58,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,107,140,152,],[39,39,62,39,39,85,86,87,88,62,62,39,39,107,107,62,62,62,62,107,107,62,62,62,62,62,107,62,39,]),'TkTrue':([17,18,39,42,67,68,69,70,75,76,107,152,],[40,40,40,40,40,40,40,40,40,40,40,40,]),'TkFalse':([17,18,39,42,67,68,69,70,75,76,107,152,],[41,41,41,41,41,41,41,41,41,41,41,41,]),'TkNot':([17,18,39,42,67,68,69,70,75,76,107,152,],[42,42,42,42,42,42,42,42,42,42,42,42,]),'TkSize':([17,18,35,39,42,58,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,107,140,152,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'TkMax':([17,18,35,39,42,58,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,107,140,152,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'TkMin':([17,18,35,39,42,58,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,107,140,152,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'TkAtoi':([17,18,35,39,42,58,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,107,140,152,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'TkNum':([17,18,35,39,42,58,62,64,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,107,137,140,143,144,152,166,],[48,48,48,48,48,48,48,101,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,155,48,159,160,48,173,]),'TkString':([19,20,35,90,91,99,],[51,51,63,51,51,63,]),'TkTwoPoints':([24,95,96,156,],[56,-15,139,-14,]),'TkComma':([24,95,101,160,],[57,138,144,144,]),'TkOd':([25,54,102,],[-2,-1,145,]),'TkGuard':([25,44,48,50,51,52,53,54,59,60,61,63,118,119,120,121,122,124,129,130,131,132,133,134,135,141,142,147,148,149,150,169,175,176,],[-2,-38,-37,-71,-75,-76,-72,-1,-18,-19,-20,-26,-27,-28,-29,-30,-31,-32,152,152,-65,-66,-67,-73,-74,-25,-21,-33,-34,-35,-36,-22,152,152,]),'TkFi':([25,44,48,50,51,52,53,54,59,60,61,63,118,119,120,121,122,124,129,130,131,132,133,134,135,141,142,147,148,149,150,151,153,154,169,175,176,179,180,],[-2,-38,-37,-71,-75,-76,-72,-1,-18,-19,-20,-26,-27,-28,-29,-30,-31,-32,-11,-11,-65,-66,-67,-73,-74,-25,-21,-33,-34,-35,-36,163,-70,165,-22,-11,-11,-68,-69,]),'TkRof':([25,54,174,],[-2,-1,178,]),'TkIn':([34,],[58,]),'TkOBracket':([35,94,],[64,137,]),'TkArrow':([37,40,41,44,48,49,84,103,104,105,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,147,148,149,150,158,164,],[66,-54,-55,-38,-37,89,-56,-43,-44,-48,-47,-52,-51,-39,-40,-41,-42,-45,-46,-49,-50,-27,-28,-29,-30,-31,-53,-32,-33,-34,-35,-36,168,171,]),'TkOr':([37,40,41,44,48,49,82,84,103,104,105,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,147,148,149,150,164,],[67,-54,-55,-38,-37,67,67,-56,-43,-44,67,-47,67,-51,-39,-40,-41,-42,-45,67,-49,67,-27,-28,-29,-30,-31,-53,-32,-33,-34,-35,-36,67,]),'TkAnd':([37,40,41,44,48,49,82,84,103,104,105,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,147,148,149,150,164,],[68,-54,-55,-38,-37,68,68,-56,-43,-44,68,-47,68,-51,-39,-40,-41,-42,-45,68,-49,68,-27,-28,-29,-30,-31,-53,-32,-33,-34,-35,-36,68,]),'TkEqual':([37,38,40,41,44,48,49,82,83,84,103,104,105,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,146,147,148,149,150,164,],[69,75,-54,-55,-38,-37,69,69,75,-56,-43,-44,-48,-47,-52,-51,-39,-40,-41,-42,-45,-46,-49,-50,-27,-28,-29,-30,-31,-53,-32,75,-33,-34,-35,-36,69,]),'TkNEqual':([37,38,40,41,44,48,49,82,83,84,103,104,105,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,146,147,148,149,150,164,],[70,76,-54,-55,-38,-37,70,70,76,-56,-43,-44,-48,-47,-52,-51,-39,-40,-41,-42,-45,-46,-49,-50,-27,-28,-29,-30,-31,-53,-32,76,-33,-34,-35,-36,70,]),'TkLess':([38,44,48,83,106,109,114,116,118,119,120,121,122,124,146,147,148,149,150,],[71,-38,-37,71,71,71,71,71,-27,-28,-29,-30,-31,-32,71,-33,-34,-35,-36,]),'TkLeq':([38,44,48,83,106,109,114,116,118,119,120,121,122,124,146,147,148,149,150,],[72,-38,-37,72,72,72,72,72,-27,-28,-29,-30,-31,-32,72,-33,-34,-35,-36,]),'TkGeq':([38,44,48,83,106,109,114,116,118,119,120,121,122,124,146,147,148,149,150,],[73,-38,-37,73,73,73,73,73,-27,-28,-29,-30,-31,-32,73,-33,-34,-35,-36,]),'TkGreater':([38,44,48,83,106,109,114,116,118,119,120,121,122,124,146,147,148,149,150,],[74,-38,-37,74,74,74,74,74,-27,-28,-29,-30,-31,-32,74,-33,-34,-35,-36,]),'TkPlus':([38,44,48,59,83,97,98,106,109,110,111,112,113,114,116,118,119,120,121,122,124,146,147,148,149,150,158,],[77,-38,-37,77,77,77,77,77,77,77,77,77,77,77,77,-27,-28,-29,-30,-31,-32,77,-33,-34,-35,-36,77,]),'TkMinus':([38,44,48,59,83,97,98,106,109,110,111,112,113,114,116,118,119,120,121,122,124,146,147,148,149,150,158,],[78,-38,-37,78,78,78,78,78,78,78,78,78,78,78,78,-27,-28,-29,-30,-31,-32,78,-33,-34,-35,-36,78,]),'TkMult':([38,44,48,59,83,97,98,106,109,110,111,112,113,114,116,118,119,120,121,122,124,146,147,148,149,150,158,],[79,-38,-37,79,79,79,79,79,79,79,79,79,79,79,79,79,79,-29,-30,-31,-32,79,-33,-34,-35,-36,79,]),'TkDiv':([38,44,48,59,83,97,98,106,109,110,111,112,113,114,116,118,119,120,121,122,124,146,147,148,149,150,158,],[80,-38,-37,80,80,80,80,80,80,80,80,80,80,80,80,80,80,-29,-30,-31,-32,80,-33,-34,-35,-36,80,]),'TkMod':([38,44,48,59,83,97,98,106,109,110,111,112,113,114,116,118,119,120,121,122,124,146,147,148,149,150,158,],[81,-38,-37,81,81,81,81,81,81,81,81,81,81,81,81,81,81,-29,-30,-31,-32,81,-33,-34,-35,-36,81,]),'TkClosePar':([40,41,44,48,82,83,84,98,103,104,105,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,146,147,148,149,150,],[-54,-55,-38,-37,123,124,-56,124,-43,-44,-48,-47,-52,-51,-39,-40,-41,-42,-45,-46,-49,-50,-27,-28,-29,-30,-31,-53,-32,147,148,149,150,124,-33,-34,-35,-36,]),'TkTo':([44,48,97,118,119,120,121,122,124,147,148,149,150,],[-38,-37,140,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,]),'TkConcat':([51,52,63,],[90,91,99,]),'TkInt':([56,139,],[93,93,]),'TkArray':([56,139,],[94,94,]),'TkCBracket':([100,101,159,160,161,173,],[142,-24,169,-24,-23,177,]),'TkSoForth':([101,155,],[143,166,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'block':([0,66,89,168,171,],[1,102,130,174,176,]),'body':([2,3,5,6,7,8,9,22,],[4,23,26,27,28,29,30,23,]),'sentence':([2,3,5,6,7,8,9,22,],[5,5,5,5,5,5,5,5,]),'gfor':([2,3,5,6,7,8,9,22,],[6,6,6,6,6,6,6,6,]),'read':([2,3,5,6,7,8,9,22,],[7,7,7,7,7,7,7,7,]),'gdo':([2,3,5,6,7,8,9,22,],[8,8,8,8,8,8,8,8,]),'gif':([2,3,5,6,7,8,9,22,],[9,9,9,9,9,9,9,9,]),'empty':([2,3,5,6,7,8,9,22,129,130,175,176,],[10,10,10,10,10,10,10,10,153,153,153,153,]),'assign':([2,3,5,6,7,8,9,22,89,171,],[11,11,11,11,11,11,11,11,131,131,]),'gprint':([2,3,5,6,7,8,9,22,89,171,],[12,12,12,12,12,12,12,12,132,132,]),'gprintln':([2,3,5,6,7,8,9,22,89,171,],[13,13,13,13,13,13,13,13,133,133,]),'start':([3,22,],[21,55,]),'declaration':([3,22,],[22,22,]),'boolean':([17,18,39,42,67,68,69,70,75,76,107,152,],[37,49,82,84,103,104,105,108,115,117,82,164,]),'expression':([17,18,35,39,42,58,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,107,140,152,],[38,38,59,83,38,97,98,38,38,106,109,110,111,112,113,114,116,118,119,120,121,122,146,158,38,]),'strprint':([19,20,90,91,],[50,53,134,135,]),'strexp':([35,99,],[60,141,]),'array':([35,],[61,]),'tipo':([56,139,],[92,157,]),'listaid':([57,138,],[96,156,]),'inarray':([64,144,],[100,161,]),'unique':([89,171,],[129,175,]),'guard':([129,130,175,176,],[151,154,179,180,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> block","S'",1,None,None,None),
  ('block -> TkOBlock TkDeclare start TkCBlock','block',4,'p_code','parser.py',28),
  ('block -> TkOBlock body TkCBlock','block',3,'p_code','parser.py',29),
  ('body -> sentence body','body',2,'p_body','parser.py',38),
  ('body -> gfor body','body',2,'p_body','parser.py',39),
  ('body -> read body','body',2,'p_body','parser.py',40),
  ('body -> gdo body','body',2,'p_body','parser.py',41),
  ('body -> gif body','body',2,'p_body','parser.py',42),
  ('body -> empty','body',1,'p_body','parser.py',43),
  ('start -> declaration start','start',2,'p_start','parser.py',47),
  ('start -> body','start',1,'p_start','parser.py',48),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',52),
  ('declaration -> TkId TkTwoPoints tipo TkSemiColon','declaration',4,'p_declaration','parser.py',56),
  ('declaration -> TkId TkComma listaid TkTwoPoints tipo TkSemiColon','declaration',6,'p_declaration','parser.py',57),
  ('listaid -> TkId TkComma listaid','listaid',3,'p_listid','parser.py',64),
  ('listaid -> TkId','listaid',1,'p_listid','parser.py',65),
  ('tipo -> TkInt','tipo',1,'p_tipo','parser.py',72),
  ('tipo -> TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket','tipo',6,'p_tipo','parser.py',73),
  ('assign -> TkId TkAsig expression','assign',3,'p_assign_expr','parser.py',76),
  ('assign -> TkId TkAsig strexp','assign',3,'p_assign_str','parser.py',81),
  ('assign -> TkId TkAsig array','assign',3,'p_assign_arr','parser.py',86),
  ('array -> TkOBracket inarray TkCBracket','array',3,'p_array','parser.py',91),
  ('array -> TkOBracket TkNum TkSoForth TkNum TkCBracket','array',5,'p_array','parser.py',92),
  ('inarray -> TkNum TkComma inarray','inarray',3,'p_iarray','parser.py',95),
  ('inarray -> TkNum','inarray',1,'p_iarray','parser.py',96),
  ('strexp -> TkString TkConcat strexp','strexp',3,'p_expression_str','parser.py',99),
  ('strexp -> TkString','strexp',1,'p_expression_str','parser.py',100),
  ('expression -> expression TkPlus expression','expression',3,'p_expression_bin','parser.py',103),
  ('expression -> expression TkMinus expression','expression',3,'p_expression_bin','parser.py',104),
  ('expression -> expression TkMult expression','expression',3,'p_expression_bin','parser.py',105),
  ('expression -> expression TkDiv expression','expression',3,'p_expression_bin','parser.py',106),
  ('expression -> expression TkMod expression','expression',3,'p_expression_bin','parser.py',107),
  ('expression -> TkOpenPar expression TkClosePar','expression',3,'p_expression_group','parser.py',120),
  ('expression -> TkSize TkOpenPar TkId TkClosePar','expression',4,'p_expression_fun','parser.py',124),
  ('expression -> TkMax TkOpenPar TkId TkClosePar','expression',4,'p_expression_fun','parser.py',125),
  ('expression -> TkMin TkOpenPar TkId TkClosePar','expression',4,'p_expression_fun','parser.py',126),
  ('expression -> TkAtoi TkOpenPar TkId TkClosePar','expression',4,'p_expression_fun','parser.py',127),
  ('expression -> TkNum','expression',1,'p_expression_number','parser.py',131),
  ('expression -> TkId','expression',1,'p_expression_id','parser.py',136),
  ('boolean -> expression TkLess expression','boolean',3,'p_boolean_exp','parser.py',145),
  ('boolean -> expression TkLeq expression','boolean',3,'p_boolean_exp','parser.py',146),
  ('boolean -> expression TkGeq expression','boolean',3,'p_boolean_exp','parser.py',147),
  ('boolean -> expression TkGreater expression','boolean',3,'p_boolean_exp','parser.py',148),
  ('boolean -> boolean TkOr boolean','boolean',3,'p_boolean_exp','parser.py',149),
  ('boolean -> boolean TkAnd boolean','boolean',3,'p_boolean_exp','parser.py',150),
  ('boolean -> expression TkEqual expression','boolean',3,'p_boolean_exp','parser.py',151),
  ('boolean -> expression TkEqual boolean','boolean',3,'p_boolean_exp','parser.py',152),
  ('boolean -> boolean TkEqual expression','boolean',3,'p_boolean_exp','parser.py',153),
  ('boolean -> boolean TkEqual boolean','boolean',3,'p_boolean_exp','parser.py',154),
  ('boolean -> expression TkNEqual expression','boolean',3,'p_boolean_exp','parser.py',155),
  ('boolean -> expression TkNEqual boolean','boolean',3,'p_boolean_exp','parser.py',156),
  ('boolean -> boolean TkNEqual expression','boolean',3,'p_boolean_exp','parser.py',157),
  ('boolean -> boolean TkNEqual boolean','boolean',3,'p_boolean_exp','parser.py',158),
  ('boolean -> TkOpenPar boolean TkClosePar','boolean',3,'p_boolean_group','parser.py',171),
  ('boolean -> TkTrue','boolean',1,'p_boolean_true','parser.py',176),
  ('boolean -> TkFalse','boolean',1,'p_boolean_false','parser.py',181),
  ('boolean -> TkNot boolean','boolean',2,'p_boolean_not','parser.py',186),
  ('read -> TkRead TkId TkSemiColon','read',3,'p_read','parser.py',190),
  ('gfor -> TkFor TkId TkIn expression TkTo expression TkArrow block TkRof TkSemiColon','gfor',10,'p_cycle_for','parser.py',194),
  ('gdo -> TkDo boolean TkArrow block TkOd TkSemiColon','gdo',6,'p_cycle_do','parser.py',197),
  ('gif -> TkIf boolean TkArrow unique guard TkFi TkSemiColon','gif',7,'p_if','parser.py',200),
  ('gif -> TkIf boolean TkArrow block guard TkFi TkSemiColon','gif',7,'p_if','parser.py',201),
  ('sentence -> assign TkSemiColon','sentence',2,'p_sentence','parser.py',204),
  ('sentence -> gprint TkSemiColon','sentence',2,'p_sentence','parser.py',205),
  ('sentence -> gprintln TkSemiColon','sentence',2,'p_sentence','parser.py',206),
  ('unique -> assign','unique',1,'p_unique','parser.py',208),
  ('unique -> gprint','unique',1,'p_unique','parser.py',209),
  ('unique -> gprintln','unique',1,'p_unique','parser.py',210),
  ('guard -> TkGuard boolean TkArrow unique guard','guard',5,'p_guard','parser.py',213),
  ('guard -> TkGuard boolean TkArrow block guard','guard',5,'p_guard','parser.py',214),
  ('guard -> empty','guard',1,'p_guard','parser.py',215),
  ('gprint -> TkPrint strprint','gprint',2,'p_print','parser.py',218),
  ('gprintln -> TkPrintln strprint','gprintln',2,'p_println','parser.py',221),
  ('strprint -> TkString TkConcat strprint','strprint',3,'p_strprint','parser.py',224),
  ('strprint -> TkId TkConcat strprint','strprint',3,'p_strprint','parser.py',225),
  ('strprint -> TkString','strprint',1,'p_strprint','parser.py',226),
  ('strprint -> TkId','strprint',1,'p_strprint','parser.py',227),
]
