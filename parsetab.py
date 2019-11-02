
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftTkAsignonassocTkLessTkLeqTkGeqTkGreaterleftTkPlusTkMinusleftTkMultTkDivTkModleftTkEqualTkNEqualleftTkAndTkOrrightTkNotleftTkOBracketTkCBracketleftTkConcatrightTkArrowTkAnd TkArray TkArrow TkAsig TkAtoi TkCBlock TkCBracket TkClosePar TkComma TkConcat TkDeclare TkDiv TkDo TkEqual TkFalse TkFi TkFor TkGeq TkGreater TkGuard TkId TkIf TkIn TkInt TkLeq TkLess TkMax TkMin TkMinus TkMod TkMult TkNEqual TkNot TkNum TkOBlock TkOBracket TkOd TkOpenPar TkOr TkPlus TkPrint TkPrintln TkRead TkRof TkSemiColon TkSize TkSoForth TkString TkTo TkTrue TkTwoPointsdeclaration : TkId TkTwoPoints TkInt TkSemiColonassign : TkId TkAsig expression TkSemiColonexpression : expression TkPlus expression TkSemiColon\n                  | expression TkMinus expression TkSemiColon\n                  | expression TkMult expression TkSemiColon\n                  | expression TkDiv expression TkSemiColon\n                  | expression TkMod expression TkSemiColon\n                  | expression TkLess expression TkSemiColon\n                  | expression TkLeq expression TkSemiColon\n                  | expression TkGeq expression TkSemiColon\n                  | expression TkGreater expression TkSemiColonexpression : TkOpenPar expression TkCloseParexpression : TkNum TkSemiColonexpression : TkId TkSemiColon'
    
_lr_action_items = {'TkId':([0,],[2,]),'$end':([1,5,],[0,-1,]),'TkTwoPoints':([2,],[3,]),'TkInt':([3,],[4,]),'TkSemiColon':([4,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaration':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaration","S'",1,None,None,None),
  ('declaration -> TkId TkTwoPoints TkInt TkSemiColon','declaration',4,'p_declaration','parser.py',31),
  ('assign -> TkId TkAsig expression TkSemiColon','assign',4,'p_assign_expr','parser.py',41),
  ('expression -> expression TkPlus expression TkSemiColon','expression',4,'p_expression_bin','parser.py',65),
  ('expression -> expression TkMinus expression TkSemiColon','expression',4,'p_expression_bin','parser.py',66),
  ('expression -> expression TkMult expression TkSemiColon','expression',4,'p_expression_bin','parser.py',67),
  ('expression -> expression TkDiv expression TkSemiColon','expression',4,'p_expression_bin','parser.py',68),
  ('expression -> expression TkMod expression TkSemiColon','expression',4,'p_expression_bin','parser.py',69),
  ('expression -> expression TkLess expression TkSemiColon','expression',4,'p_expression_bin','parser.py',70),
  ('expression -> expression TkLeq expression TkSemiColon','expression',4,'p_expression_bin','parser.py',71),
  ('expression -> expression TkGeq expression TkSemiColon','expression',4,'p_expression_bin','parser.py',72),
  ('expression -> expression TkGreater expression TkSemiColon','expression',4,'p_expression_bin','parser.py',73),
  ('expression -> TkOpenPar expression TkClosePar','expression',3,'p_expression_group','parser.py',87),
  ('expression -> TkNum TkSemiColon','expression',2,'p_expression_number','parser.py',91),
  ('expression -> TkId TkSemiColon','expression',2,'p_expression_id','parser.py',96),
]
