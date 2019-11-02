
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftTkAsignonassocTkLessTkLeqTkGeqTkGreaterleftTkPlusTkMinusleftTkMultTkDivTkModleftTkEqualTkNEqualleftTkAndTkOrrightTkNotleftTkOBracketTkCBracketleftTkConcatrightTkArrowTkAnd TkArray TkArrow TkAsig TkAtoi TkCBlock TkCBracket TkClosePar TkComma TkConcat TkDeclare TkDiv TkDo TkEqual TkFalse TkFi TkFor TkGeq TkGreater TkGuard TkId TkIf TkIn TkInt TkLeq TkLess TkMax TkMin TkMinus TkMod TkMult TkNEqual TkNot TkNum TkOBlock TkOBracket TkOd TkOpenPar TkOr TkPlus TkPrint TkPrintln TkRead TkRof TkSemiColon TkSize TkSoForth TkString TkTo TkTrue TkTwoPoints start : declaration start\n              | assign start\n              | emptyempty :declaration : TkId TkTwoPoints TkInt TkSemiColonassign : TkId TkAsig expression TkSemiColonexpression : expression TkPlus expression TkSemiColon\n                  | expression TkMinus expression TkSemiColon\n                  | expression TkMult expression TkSemiColon\n                  | expression TkDiv expression TkSemiColon\n                  | expression TkMod expression TkSemiColon\n                  | expression TkLess expression TkSemiColon\n                  | expression TkLeq expression TkSemiColon\n                  | expression TkGeq expression TkSemiColon\n                  | expression TkGreater expression TkSemiColonexpression : TkOpenPar expression TkCloseParexpression : TkNum TkSemiColonexpression : TkId TkSemiColon'
    
_lr_action_items = {'TkId':([0,2,3,9,13,15,17,18,19,20,21,22,23,24,25,26,],[5,5,5,11,11,-5,-6,11,11,11,11,11,11,11,11,11,]),'$end':([0,1,2,3,4,6,7,15,17,],[-4,0,-4,-4,-3,-1,-2,-5,-6,]),'TkTwoPoints':([5,],[8,]),'TkAsig':([5,],[9,]),'TkInt':([8,],[10,]),'TkOpenPar':([9,13,18,19,20,21,22,23,24,25,26,],[13,13,13,13,13,13,13,13,13,13,13,]),'TkNum':([9,13,18,19,20,21,22,23,24,25,26,],[14,14,14,14,14,14,14,14,14,14,14,]),'TkSemiColon':([10,11,12,14,16,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[15,16,17,28,-18,-17,39,40,41,42,43,44,45,46,47,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'TkPlus':([12,16,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[18,-18,18,-17,18,18,18,18,18,18,18,18,18,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'TkMinus':([12,16,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[19,-18,19,-17,19,19,19,19,19,19,19,19,19,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'TkMult':([12,16,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[20,-18,20,-17,20,20,20,20,20,20,20,20,20,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'TkDiv':([12,16,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[21,-18,21,-17,21,21,21,21,21,21,21,21,21,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'TkMod':([12,16,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[22,-18,22,-17,22,22,22,22,22,22,22,22,22,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'TkLess':([12,16,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[23,-18,23,-17,23,23,23,23,23,23,23,23,23,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'TkLeq':([12,16,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[24,-18,24,-17,24,24,24,24,24,24,24,24,24,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'TkGeq':([12,16,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[25,-18,25,-17,25,25,25,25,25,25,25,25,25,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'TkGreater':([12,16,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[26,-18,26,-17,26,26,26,26,26,26,26,26,26,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'TkClosePar':([16,27,28,38,39,40,41,42,43,44,45,46,47,],[-18,38,-17,-16,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,2,3,],[1,6,7,]),'declaration':([0,2,3,],[2,2,2,]),'assign':([0,2,3,],[3,3,3,]),'empty':([0,2,3,],[4,4,4,]),'expression':([9,13,18,19,20,21,22,23,24,25,26,],[12,27,29,30,31,32,33,34,35,36,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> declaration start','start',2,'p_start','parser.py',31),
  ('start -> assign start','start',2,'p_start','parser.py',32),
  ('start -> empty','start',1,'p_start','parser.py',33),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',36),
  ('declaration -> TkId TkTwoPoints TkInt TkSemiColon','declaration',4,'p_declaration','parser.py',40),
  ('assign -> TkId TkAsig expression TkSemiColon','assign',4,'p_assign_expr','parser.py',50),
  ('expression -> expression TkPlus expression TkSemiColon','expression',4,'p_expression_bin','parser.py',74),
  ('expression -> expression TkMinus expression TkSemiColon','expression',4,'p_expression_bin','parser.py',75),
  ('expression -> expression TkMult expression TkSemiColon','expression',4,'p_expression_bin','parser.py',76),
  ('expression -> expression TkDiv expression TkSemiColon','expression',4,'p_expression_bin','parser.py',77),
  ('expression -> expression TkMod expression TkSemiColon','expression',4,'p_expression_bin','parser.py',78),
  ('expression -> expression TkLess expression TkSemiColon','expression',4,'p_expression_bin','parser.py',79),
  ('expression -> expression TkLeq expression TkSemiColon','expression',4,'p_expression_bin','parser.py',80),
  ('expression -> expression TkGeq expression TkSemiColon','expression',4,'p_expression_bin','parser.py',81),
  ('expression -> expression TkGreater expression TkSemiColon','expression',4,'p_expression_bin','parser.py',82),
  ('expression -> TkOpenPar expression TkClosePar','expression',3,'p_expression_group','parser.py',96),
  ('expression -> TkNum TkSemiColon','expression',2,'p_expression_number','parser.py',100),
  ('expression -> TkId TkSemiColon','expression',2,'p_expression_id','parser.py',105),
]
